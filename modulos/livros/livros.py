from flask import Blueprint, render_template, request, redirect, flash
from models import Livros, Autores
from database import db

bp_livro = Blueprint('livros', __name__, template_folder="templates")

@bp_livro.route('/')
def index():
    dados = Livros.query.all()
    return render_template('livro.html', livros = dados)

@bp_livro.route('/add')
def add():
    a = Autores.query.all()
    return render_template('livro_add.html', autores = a)

@bp_livro.route('/save', methods=['POST'])
def save():
    titulo = request.form.get('titulo')
    ano_publicacao = request.form.get('ano_publicacao')
    autor_id = request.form.get('autor_id')
    if titulo and ano_publicacao and autor_id:
        db_livro = Livros(titulo, ano_publicacao, autor_id)
        db.session.add(db_livro)
        db.session.commit()
        flash('Livro salvo com sucesso!!!')
        return redirect ('/livros')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/livros/add')
