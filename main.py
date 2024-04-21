import os
import sqlite3

from flask import Flask, render_template, redirect, flash, request
from forms import LoginForm, RegisterForm, EditProfileForm, MessageForm, AddProjectForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from data.users import User
from data.projects import Project
from data.messages import Message
from flask_sqlalchemy import SQLAlchemy
from data import db_session
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


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


@app.route('/projects')
def projects_page():
    db_sess = db_session.create_session()
    list_of_projects = db_sess.query(Project).all()
    return render_template('projects.html', title='Проекты', list_of_projects=list_of_projects)


@app.route('/projects/<int:project_id>')
def project_page(project_id):
    db_sess = db_session.create_session()
    project = db_sess.query(Project).filter(Project.id == project_id).first()
    science_leader = db_sess.query(User).filter(User.id == project.author_id).first()
    return render_template('project.html', title='Проект', s_l=science_leader, project=project)


@app.route('/add_project', methods=['GET', 'POST'])
def add_project_page():
    form = AddProjectForm()
    errors = {
        "title": [],
        "theme": [],
        "description": [],
    }
    print("111", form.validate_on_submit())
    if form.validate_on_submit():
        print('form validated on submit')
        db_sess = db_session.create_session()
        if db_sess.query(Project).filter(Project.title == form.title.data).first():
            errors["title"].append("Проект с таким названием уже существует!")
        if any(errors.values()):
            print("errors")
            return render_template('add_project.html', title='Заявка проекта', form=form, errors=errors)
        project = Project(title=form.title.data,
                          theme=form.theme.data,
                          description=form.description.data,
                          author_id=current_user.id)
        db_sess.add(project)
        db_sess.commit()
        return redirect('/')
    print('yt')
    return render_template('add_project.html', title='Заявка проекта', form=form, errors=errors)


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    message_form = MessageForm()
    db_sess = db_session.create_session()
    if request.method == 'POST' and message_form.validate_on_submit():
        new_message = Message(body=message_form.body.data,
                              project_id=2,
                              is_from_teacher=(current_user.role == 'teacher'))
        db_sess.add(new_message)
        db_sess.commit()
    message_form.body.data = ''
    project = db_sess.query(Project).get(2)
    messages = db_sess.query(Message).filter(Message.project == project).order_by(Message.date).all()
    return render_template('_chat.html', title='Чат', form=message_form, messages=messages)


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
        if form.avatar_file.data:
            form.avatar_file.data.save(os.path.join(app.config['UPLOAD_FOLDER'], current_user.email + '.png'))
            current_user.avatar_exist = True
            flash('Фото обновлено!')
        new_user = db_sess.merge(current_user)
        db_sess.add(new_user)
        db_sess.commit()
        flash('Изменения сохранены!')
        return redirect(f'/profile/{current_user.id}')
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