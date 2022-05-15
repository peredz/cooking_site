from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField,\
    StringField
from wtforms.validators import DataRequired
from werkzeug.security import check_password_hash


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

    def authorization_check(self, user):
        if user:
            if check_password_hash(user.password, self.password.data):
                return True


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    login = StringField('Логин', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    password = StringField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
