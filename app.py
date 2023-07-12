from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://snrmyrdk:WdWoPvt6qtVm9uq8V93rSYGKkf3WW-nt@tuffi.db.elephantsql.com/snrmyrdk'

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


@app.route('/')
def index():
    # posters = Posters.query.order_by("ano").all()
    # posters = Posters.query.order_by(Posters.ano.asc()).all()
    posters = Posters.query.filter(Posters.tmdb < 0).all()
    return render_template("index.html", posters=posters)


@app.route("/<id>")
def modal(id):
    print('oi')
    posterID = Posters.query.filter_by(id=id).first()
    return render_template('index.html', posterID=posterID)


@app.route('/editar/<id>', methods=["GET", "POST"])
def editar(id):
    poster = Posters.query.filter_by(id=id).first()
    if request.method == "POST":
        tmdb = request.form.get("tmdb")
        imdb = request.form.get("imdb")
        titulo_original = request.form.get("titulo_original").upper()
        titulo_traduzido = request.form.get("titulo_traduzido").upper()
        pagina = int(request.form.get("pagina"))
        data_release = request.form.get("data_release")
        ano = int(data_release[0:4])
        link_imagem = request.form.get("link_imagem")
        sinopse = request.form.get("sinopse")

        if tmdb:
            poster.tmdb = tmdb
            poster.imdb = imdb
            poster.titulo_original = titulo_original
            poster.titulo_traduzido = titulo_traduzido
            poster.pagina = pagina
            poster.data_release = data_release
            poster.ano = ano
            poster.link_imagem = link_imagem
            poster.sinopse = sinopse

            db.session.commit()
            return redirect(url_for("index"))
    return render_template("editar.html", poster=poster)


@app.route('/novo', methods=["GET", "POST"])
def novo():
    if request.method == "POST":
        tmdb = request.form.get("tmdb")
        imdb = request.form.get("imdb")
        titulo_original = request.form.get("titulo_original")
        titulo_traduzido = request.form.get("titulo_traduzido")
        pagina = int(request.form.get("pagina"))
        data_release = request.form.get("data_release")
        ano = int(data_release[0:4])
        link_imagem = request.form.get("link_imagem")
        sinopse = request.form.get("sinopse")

        if tmdb:
            p = Posters(tmdb, imdb, titulo_original, titulo_traduzido, ano, pagina, data_release, link_imagem, sinopse)
            db.session.add(p)
            db.session.commit()
            return redirect(url_for("index"))
    return render_template("novo.html")


@app.route("/excluir/<id>")
def excluir(id):
    poster = Posters.query.filter_by(id=id).first()
    db.session.delete(poster)
    db.session.commit()
    return redirect(url_for("index"))


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
