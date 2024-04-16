from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired(message="Это поле обязательно"),
                                            Email(message="Укажите действительный адрес электронной почты")])
    name = StringField('Имя', validators=[DataRequired(message="Это поле обязательно")])
    surname = StringField('Фамилия', validators=[DataRequired(message="Это поле обязательно")])
    password = PasswordField('Пароль', validators=[DataRequired(message="Это поле обязательно")])
    confirm = PasswordField('Повторите пароль', validators=[EqualTo('password', message='Пароли не совпадают')])
    submit = SubmitField('Создать аккаунт')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired(message="Это поле обязательно")])
    password = PasswordField('Пароль', validators=[DataRequired(message="Это поле обязательно")])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
