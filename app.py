from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'STRINgqUENINGUémsAbe'
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/atividade03"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLACHEMY_TRACK_MODIFICATIOS'] = False
from database import db
from flask_migrate import Migrate
from models import Autores, Livros
db.init_app(app)
migrate = Migrate(app, db)
from modulos.autores.autores import bp_autor
app.register_blueprint(bp_autor, url_prefix='/autores')
from modulos.livros.livros import bp_livro
app.register_blueprint(bp_livro, url_prefix='/livros')

@app.route('/')
def index():
    return render_template("index.html")



