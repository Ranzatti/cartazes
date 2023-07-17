from connection import db


class Posters(db.Model):
    __tablename__ = 'poster'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tmdb = db.Column(db.Integer)
    imdb = db.Column(db.String)
    titulo_original = db.Column(db.String)
    titulo_traduzido = db.Column(db.String)
    ano = db.Column(db.Integer)
    pagina = db.Column(db.Integer)
    data_release = db.Column(db.String)
    link_imagem = db.Column(db.String)
    sinopse = db.Column(db.String)

    def __init__(self, tmdb, imdb, titulo_original, titulo_traduzido, ano, pagina, data_release, link_imagem, sinopse):
        self.tmdb = tmdb
        self.imdb = imdb
        self.titulo_original = titulo_original
        self.titulo_traduzido = titulo_traduzido
        self.ano = ano
        self.pagina = pagina
        self.data_release = data_release
        self.link_imagem = link_imagem
        self.sinopse = sinopse

    def salva(id, tmdb, imdb, titulo_original, titulo_traduzido, pagina, data_release, link_imagem, sinopse):
        if int(tmdb) > 0:
            poster = Posters.query.filter_by(id=id).first()
            if poster:
                poster.tmdb = tmdb
                poster.imdb = imdb
                poster.titulo_original = titulo_original.upper()
                poster.titulo_traduzido = titulo_traduzido.upper()
                poster.pagina = int(pagina)
                poster.data_release = data_release
                poster.ano = int(poster.data_release[0:4])
                poster.link_imagem = link_imagem
                poster.sinopse = sinopse
            else:
                ano = int(data_release[0:4])
                poster = Posters(
                    tmdb,
                    imdb,
                    titulo_original.upper(),
                    titulo_traduzido.upper(),
                    ano,
                    pagina,
                    data_release,
                    link_imagem,
                    sinopse)
            db.session.add(poster)
            db.session.commit()
            return True
        return False

    def getByID(id):
        return Posters.query.filter_by(id=id).first()

    def getAll():
        posters = Posters.query.order_by("ano").all()
        # posters = Posters.query.order_by(Posters.titulo_original.asc()).all()
        # posters = Posters.query.filter(Posters.tmdb < 0).all()
        return posters

    def exclui(id):
        poster = Posters.query.filter_by(id=id).first()
        db.session.delete(poster)
        db.session.commit()

    def create():
        db.create_all()