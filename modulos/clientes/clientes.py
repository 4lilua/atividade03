from flask import Blueprint, render_template, request, redirect, flash
from models import Clientes
from database import db

bp_cliente = Blueprint('clientes', __name__, template_folder="templates")

@bp_cliente.route('/')
def index():
    dados = Clientes.query.all()
    return render_template('cliente.html', clientes = dados)

@bp_cliente.route('/add')
def add():
    return render_template('cliente_add.html')

@bp_cliente.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    telefone = request.form.get('telefone')
    if nome and telefone:
        db_cliente = Clientes(nome, telefone)
        db.session.add(db_cliente)
        db.session.commit()
        flash('Cliente salvo com sucesso!!!')
        return redirect ('/clientes')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/clientes/add')
