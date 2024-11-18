from flask import Blueprint, render_template, request, redirect, flash
from models import Autor
from database import db

bp_autor = Blueprint('autores', __name__, template_folder="templates")

@bp_autor.route('/')
def index():
    dados = Autor.query.all()
    return render_template('autor.html', autores = dados)

@bp_autor.route('/add')
def add():
    return render_template('autor_add.html')

@bp_autor.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    nacionalidade = request.form.get('nacionalidade')
    if nome and nacionalidade:
        db_autor = Autor(nome, nacionalidade)
        db.session.add(db_autor)
        db.session.commit()
        flash('Autor salvo com sucesso!!!')
        return redirect ('/autores')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/autores/add')
