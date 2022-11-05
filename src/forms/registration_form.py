from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField)
from wtforms.validators import DataRequired, EqualTo, ValidationError
from src.models.user import User

class RegistrationForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired()])
    username = StringField("Usuário", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired(), 
                             EqualTo("password_confirm",message="Senhas devem ser iguais")])
    password_confirm = PasswordField("Confirmar Senha", validators=[DataRequired()])
    submit = SubmitField("Registrar")

    #Custom email validation
    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("Esse e-mail já está sendo utilizado")

    #Custom username validation
    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError("Esse usuário já existe")