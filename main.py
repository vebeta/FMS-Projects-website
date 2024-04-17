from flask import Flask, render_template, redirect, flash, request
from forms import LoginForm, RegisterForm, EditProfileForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from data.users import User
from data.themes import Themes
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/science_projects.db")
    app.run()


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def main_page():
    return render_template('home.html', title='Главная')


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    errors = {
        "email": [],
        "password": [],
        "surname": [],
        "name": []
    }
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            errors["email"].append("Почта с таким адресом уже занята!")
        if any(errors.values()):
            return render_template("register.html", title="Регистрация", form=form, errors=errors)
        user = User(surname=form.surname.data,
                    name=form.name.data,
                    email=form.email.data,
                    role="student")
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        login_user(user)
        flash("Вы успешно зарегистрировались!")
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form, errors=errors)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    errors = {
        "email": [],
        "password": []
    }
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if not user:
            errors["email"].append("Пользователя с таким email не существует!")
        elif not user.check_password(form.password.data):
            errors["password"].append("Неверный пароль")
        if any(errors.values()):
            return render_template('login.html', title="Авторизация", form=form, errors=errors)
        login_user(user, remember=form.remember_me.data)
        flash("Вы успешно вошли!")
        return redirect("/")
    return render_template('login.html', title='Авторизация', form=form, errors=errors)


@app.route('/profile/<int:user_id>')
@login_required
def profile(user_id):
    user = load_user(user_id)
    if not user:
        return redirect('/')
    return render_template("profile.html", title="Профиль", user=user)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    errors = {
        "surname": [],
        "name": []
    }
    db_sess = db_session.create_session()
    form.email.data = current_user.email
    if form.validate_on_submit():
        current_user.surname = form.surname.data
        current_user.name = form.name.data
        if form.password.data:
            current_user.set_password(form.password.data)
        db_sess.add(current_user)
        db_sess.commit()
        flash('Изменения сохранены!')
        return redirect(f"/profile/{current_user.id}")
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.surname.data = current_user.surname
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form, errors=errors)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    main()
