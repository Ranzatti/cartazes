from flask import render_template, request, url_for, redirect
from connection import app
from model import Posters


@app.route('/')
@app.route("/index")
def index():
    posters = Posters.getAll()
    return render_template("index.html", posters=posters)


@app.route('/editar/<id>', methods=["GET", "POST"])
def editar(id):
    poster = Posters.getByID(id)
    if request.method == "POST":
        if Posters.salva(
                id,
                request.form.get("tmdb"),
                request.form.get("imdb"),
                request.form.get("titulo_original"),
                request.form.get("titulo_traduzido"),
                request.form.get("pagina"),
                request.form.get("data_release"),
                request.form.get("link_imagem"),
                request.form.get("sinopse")
        ):
            return redirect(url_for("index"))
    return render_template("editar.html", poster=poster)


@app.route('/novo', methods=["GET", "POST"])
def novo():
    if request.method == "POST":
        if Posters.salva(
                -1,
                request.form.get("tmdb"),
                request.form.get("imdb"),
                request.form.get("titulo_original"),
                request.form.get("titulo_traduzido"),
                request.form.get("pagina"),
                request.form.get("data_release"),
                request.form.get("link_imagem"),
                request.form.get("sinopse")
        ):
            return redirect(url_for("index"))
    return render_template("novo.html")


@app.route("/excluir/<id>", methods=["GET"])
def excluir(id):
    if request.method == "GET":
        Posters.exclui(id)
    return redirect(url_for("index"))


with app.app_context():
    Posters.create()

if __name__ == '__main__':
    app.run(debug=True)
