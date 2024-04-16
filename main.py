from flask import Flask, render_template, redirect, flash
from forms import LoginForm, RegisterForm
from flask_login import LoginManager, login_user, logout_user, login_required
from data.users import User
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
        print(errors)
        if any(errors.values()):
            return render_template("register.html", title="Регистрация", form=form, errors=errors)
        user = User(surname=form.surname.data,
                    name=form.name.data,
                    email=form.email.data)
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
        "email": list(form.email.errors),
        "password": list(form.password.errors)
    }
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if not user:
            errors["email"].append("Пользователя с таким email не существует!")
        if not user.check_password(form.password.data):
            errors["password"].append("Неверный пароль")
        if any(errors.values()):
            return render_template('login.html', title="Авторизация", form=form, errors=errors)
        login_user(user, remember=form.remember_me.data)
        flash("Вы успешно вошли!")
        return redirect("/")
    return render_template('login.html', title='Авторизация', form=form, errors=errors)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    main()
