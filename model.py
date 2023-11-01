from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

class Posters(db.Model):
    __tablename__ = 'poster'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tmdb = db.Column(db.Integer)
    imdb = db.Column(db.String)
    titulo_original = db.Column(db.String)
    titulo_traduzido = db.Column(db.String)
    ano = db.Column(db.Integer)
    pagina = db.Column(db.Integer)
    pasta = db.Column(db.Integer)
    data_release = db.Column(db.String)
    link_imagem = db.Column(db.String)
    sinopse = db.Column(db.String)
    cores = db.Column(db.String)

    def __init__(self, tmdb, imdb, titulo_original, titulo_traduzido, ano, pagina, pasta, data_release, link_imagem, sinopse, cores):
        self.tmdb = tmdb
        self.imdb = imdb
        self.titulo_original = titulo_original
        self.titulo_traduzido = titulo_traduzido
        self.ano = ano
        self.pagina = pagina
        self.pasta = pasta
        self.data_release = data_release
        self.link_imagem = link_imagem
        self.sinopse = sinopse
        self.cores = cores

    def salva(id, tmdb, imdb, titulo_original, titulo_traduzido, pagina, pasta, data_release, link_imagem, sinopse,  cores):
        ano = int(data_release[0:4])
        poster = Posters.query.filter_by(id=id).first()
        if poster:
            poster.tmdb = tmdb
            poster.imdb = imdb
            poster.titulo_original = titulo_original.upper()
            poster.titulo_traduzido = titulo_traduzido.upper()
            poster.pagina = int(pagina)
            poster.pasta = int(pasta)
            poster.data_release = data_release
            poster.ano = ano
            poster.link_imagem = link_imagem
            poster.sinopse = sinopse
            poster.cores = cores
        else:
            poster = Posters(
                tmdb,
                imdb,
                titulo_original.upper(),
                titulo_traduzido.upper(),
                ano,
                pagina,
                pasta,
                data_release,
                link_imagem,
                sinopse,
                cores)
        db.session.add(poster)
        db.session.commit()
        return True

    def getByID(id):
        return Posters.query.filter_by(id=id).first()

    def getAll():
        posters = Posters.query.order_by("ano").all()
        # posters = Posters.query.order_by("ano").limit(30).all()
        # posters = Posters.query.order_by(Posters.titulo_original.asc()).all()
        return posters

    def exclui(id):
        poster = Posters.query.filter_by(id=id).first()
        db.session.delete(poster)
        db.session.commit()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique = True)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)
    name = db.Column(db.String)

    def __init__(self, username, email, password, name):
        self.username = username
        self.email = email
        self.password = password
        self.name = name