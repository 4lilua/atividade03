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

@bp_livro.route("/remove/<int:id>")
def remove(id):
    dados = Livros.query.get(id)
    if id > 0:
        db.session.delete(dados)
        db.session.commit()
        flash('Livro removido com sucesso!')
        return redirect("/livros")
    else:
        flash("Caminho incorreto!")
        return redirect("/livros")

@bp_livro.route("/edita/<int:id>")
def edita(id):
    livro = Livros.query.get(id)
    autor = Autores.query.all()
    return render_template("livro_edita.html", dados=livro, autor=autor)

@bp_livro.route("/editasave", methods=['POST'])
def editasave():
    id = request.form.get('id')
    titulo = request.form.get('titulo')
    ano_publicacao = request.form.get('ano_publicacao')
    autor_id = request.form.get('autor_id')
    if id and titulo and ano_publicacao and autor_id:
        livro = Livros.query.get(id)
        livro.titulo = titulo
        livro.ano_publicacao = ano_publicacao
        livro.autor_id = autor_id
        db.session.commit()
        flash('Dados atualizados com sucesso!')
        return redirect('/livros')
    else:
        flash('Dados incompletos.')
        return redirect("/livros")