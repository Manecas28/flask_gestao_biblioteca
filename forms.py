from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField
from wtforms.validators import DataRequired, NumberRange, EqualTo

class LivroForm(FlaskForm):
    titulo = StringField('Titulo', validators=[DataRequired()])
    autor = StringField('Autor', validators=[DataRequired()])
    ano = IntegerField('Ano', validators=[NumberRange(min=1500, max=2100)])
    submeter = SubmitField('Gravar')

# Classes para fazer login e Registo nas aplicações

class LoginForm(FlaskForm):

    username = StringField('Utilizador', validators= [DataRequired()])
    password = PasswordField('Password', validators= [DataRequired()])
    submeter = SubmitField('Entrar')

class RegistoForm(FlaskForm):
    
    nome = StringField('Nome', validators= [DataRequired()])
    username = StringField('Utilizador', validators= [DataRequired()])
    password = PasswordField('Password', validators= [DataRequired()])
    confirmar = PasswordField('Confirmar Password', validators= [EqualTo('password')])
    submeter = SubmitField('Registar')

