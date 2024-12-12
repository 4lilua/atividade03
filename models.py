from database import db

class Autores(db.Model):
    __tablename__ = 'autor'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    nacionalidade = db.Column(db.String(50))

    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade

    def __repr__(self):
        return "<Autor {}>".format(self.nome)

class Livros(db.Model):
    __tablename__ = 'livro'
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(100))
    ano_publicacao = db.Column(db.Integer)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id'))
    
    autor = db.relationship('Autores', foreign_keys=id_autor)

    def __init__(self, titulo, ano_publicacao, id_autor):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.id_autor = id_autor

    def __repr__(self):
        return "<Livro {}>".format(self.titulo)
