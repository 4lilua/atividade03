from database import db

class Autor(db.Model):
    __tablename__ = 'autor'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    nacionalidade = db.Column(db.String(50))

    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade

    def __repr__(self):
        return "<Autor {}>".format(self.nome)

class Livro(db.Model):
    __tablename__ = 'livro'
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(100))
    ano_publicacao = db.Column(db.Integer)
    autor_id = db.Column(db.Integer, db.ForeignKey('autor.id'))

    autor = db.relationship('Autor', foreign_keys=autor_id)

    def __init__(self, titulo, ano_publicacao, autor_id):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.autor_id = autor_id

    def __repr__(self):
        return "<Livro {} - Autor {}>".format(self.titulo, self.autor_id)

