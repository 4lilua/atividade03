from flask import Blueprint, render_template, request, redirect, flash
from models import Reclamacoes, Clientes
from database import db

bp_reclamacao = Blueprint('reclamacoes', __name__, template_folder="templates")

@bp_reclamacao.route('/')
def index():
    dados = Reclamacoes.query.all()
    return render_template('reclamacao.html', reclamacoes = dados)

@bp_reclamacao.route('/add')
def add():
    c = Clientes.query.all()
    return render_template('cliente_add.html', clientes = c)

@bp_reclamacao.route('/save', methods=['POST'])
def save():
    descricao = request.form.get('descricao')
    data = request.form.get('data')
    id_cliente = request.form.get('id_cliente')
    if descricao and data and id_cliente:
        db_reclamacao = Reclamacoes(descricao, data, id_cliente)
        db.session.add(db_reclamacao)
        db.session.commit()
        flash('Reclamação salva com sucesso!!!')
        return redirect ('/reclamacoes')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/reclamacoes/add')

@bp_reclamacao.route("/remove/<int:id>")
def remove(id):
    dados = Reclamacoes.query.get(id)
    if id > 0:
        db.session.delete(dados)
        db.session.commit()
        flash('Excluído com sucesso')
        return redirect("/reclamacoes")
    else:
        flash("Item não encontrado")
        return redirect("/reclamacoes")
