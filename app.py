from flask import Flask, render_template, redirect, url_for, request
from models import db, Livro
from forms import LivroForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.secret_key = 'segredomuitobemguardado'
db.init_app(app)

# Criar a Base de dados
@app.before_request
def criar_bd():
    db.create_all()

@app.route('/')
def index():
    return redirect(url_for('listar'))

@app.route('/livros')
def listar():
    livros = Livro.query.all()
    return render_template('lista.html', livros=livros)

@app.route('/livros/adicionar', methods=['GET', 'POST'])
def adicionar():
    form = LivroForm()
    if form.validate_on_submit():
        livro = Livro(titulo=form.titulo.data, autor=form.autor.data, ano=form.ano.data)
        db.session.add(livro)
        db.session.commit()
        return redirect(url_for('listar'))
    return render_template('adicionar.html', form=form)

@app.route('/livros/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    livro = Livro.query.get_or_404(id)
    form = LivroForm(obj=livro)
    if form.validate_on_submit():
        form.populate_obj(livro)
        db.session.commit()
        return redirect(url_for('listar'))
    return render_template('editar.html', form=form)

@app.route('/livros/apagar/<int:id>')
def apagar(id):
    livro = Livro.query.get_or_404(id)
    db.session.delete(livro)
    db.session.commit()
    return redirect(url_for('listar'))

if __name__ == "__main__":
    app.run(debug=True)