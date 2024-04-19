from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, BooleanField, FileField
from wtforms.validators import DataRequired, EqualTo, Email


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm = PasswordField('Повторите пароль', validators=[EqualTo('password')])
    submit = SubmitField('Создать аккаунт')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class EditProfileForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired(message="Это поле обязательно"),
                                            Email(message="Укажите действительный адрес электронной почты")])
    surname = StringField('Фамилия', validators=[DataRequired(message="Это поле обязательно")])
    name = StringField('Имя', validators=[DataRequired(message="Это поле обязательно")])
    password = PasswordField('Пароль')
    confirm = PasswordField('Повторите пароль', validators=[EqualTo('password', message='Пароли не совпадают')])
    submit = SubmitField('Сохранить изменения')

class Add_Project(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    title = StringField('Название', validators=[DataRequired()])
    theme = StringField('Тема', validators=[DataRequired()])
    description = StringField('Описание', validators=[DataRequired()])
    submit = SubmitField('Подать заявку')