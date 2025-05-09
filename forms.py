from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class LivroForm(FlaskForm):
    titulo = StringField('Titulo', validators=[DataRequired()])
    autor = StringField('Autor', validators=[DataRequired()])
    ano = IntegerField('Ano', validators=[NumberRange(min=1500, max=2100)])
    submeter = SubmitField('Gravar')

# Classes para fazer login e Registo nas aplicações



