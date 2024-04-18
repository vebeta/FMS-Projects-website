from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo


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


class Add_Project(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    title = StringField('Название', validators=[DataRequired()])
    theme = StringField('Тема', validators=[DataRequired()])
    description = StringField('Описание', validators=[DataRequired()])
    submit = SubmitField('Подать заявку')