from database import db

class Clientes(db.Model):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    telefone = db.Column(db.String(15))

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __repr__(self):
        return "<Cliente: {}>".format(self.nome)

class Reclamacoes(db.Model):
    __tablename__ = 'reclamacao'
    id = db.Column(db.Integer, primary_key = True)
    descricao = db.Column(db.String(225))
    data = db.Column(db.Date)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))

    autor = db.relationship('Clientes', foreign_keys=id_cliente)

    def __init__(self, descricao, data, id_cliente):
        self.descricao = descricao
        self.data = data 
        self.id_cliente = id_cliente

    def __repr__(self):
        return "<Reclamação: {}>".format(self.descricao)
