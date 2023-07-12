from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://snrmyrdk:WdWoPvt6qtVm9uq8V93rSYGKkf3WW-nt@tuffi.db.elephantsql.com/snrmyrdk'

db = SQLAlchemy(app)

class Poster(db.Model):
    __tablename__ = 'poster'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    titulo_original = db.Column(db.String)
    ano = db.Column(db.Integer)

    def __init__(self, nome, titulo_original, ano):
        self.nome = nome
        self.titulo_original = titulo_original
        self.ano = ano