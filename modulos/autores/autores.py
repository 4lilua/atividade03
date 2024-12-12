from flask import Blueprint, render_template, request, redirect, flash
from models import Autores
from database import db

bp_autor = Blueprint('autores', __name__, template_folder="templates")

@bp_autor.route('/')
def index():
    dados = Autores.query.all()
    return render_template('autor.html', autores = dados)
    
@bp_autor.route('/add')
def add():
    return render_template('autor_add.html')

@bp_autor.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    nacionalidade = request.form.get('nacionalidade')
    if nome and nacionalidade:
        bd_autor = Autores(nome, nacionalidade)
        db.session.add(bd_autor)
        db.session.commit()
        flash('Autor salvo com sucesso!!!')
        return redirect('/autores')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/autores/add')
    
@bp_autor.route("/remove/<int:id>")
def remove(id):
    dados = Autores.query.get(id)
    if id > 0:
        db.session.delete(dados)
        db.session.commit()
        flash('Autor removido com sucesso!')
        return redirect("/autores")
    else:
        flash("Caminho incorreto!")
        return redirect("/autores")

@bp_autor.route("/edita/<int:id>")
def edita(id):
    autor = Autores.query.get(id)
    return render_template("autor_edita.html", dados=autor)

@bp_autor.route("/editasave", methods=['POST'])
def editasave():
    id = request.form.get('id')
    nome = request.form.get('nome')
    nacionalidade = request.form.get('nacionalidade')
    if id and nome and nacionalidade:
        livro = Autores.query.get(id)
        livro.nome = nome
        livro.nacionalidade = nacionalidade
        db.session.commit()
        flash('Dados atualizados com sucesso!')
        return redirect('/autores')
    else:
        flash('Dados incompletos.')
        return redirect("/autores")
    
    