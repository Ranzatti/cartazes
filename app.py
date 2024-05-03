from flask import render_template, request, url_for, redirect
from model import app, db, Posters


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        posters = Posters.getAll()
        return render_template("index.html", posters=posters)
    if request.method == "POST":
        pagina = request.form.get("pagina")
        pasta = request.form.get("pasta")
        cores = request.form.get("cores")

        posters = Posters.query.filter(1 == 1)
        if pagina:
            posters = posters.filter(Posters.pagina == pagina)
        if pasta:
            posters = posters.filter(Posters.pasta == pasta)
        if cores != "todos":
            posters = posters.filter(Posters.cores == cores)
        posters = posters.all()

        return render_template("index.html", posters=posters)


@app.route('/editar/<id>', methods=["GET", "POST"])
def editar(id):
    poster = Posters.getByID(id)
    if request.method == "POST":
        Posters.salva(
            id,
            request.form.get("tmdb"),
            request.form.get("imdb"),
            request.form.get("titulo_original"),
            request.form.get("titulo_traduzido"),
            request.form.get("pagina"),
            request.form.get("pasta"),
            request.form.get("data_release"),
            request.form.get("link_imagem"),
            request.form.get("sinopse"),
            request.form.get("cores")
        )
        return redirect(url_for("index"))
    return render_template("editar.html", poster=poster)

@app.route('/novo', methods=["GET", "POST"])
def novo():
    if request.method == "POST":
        Posters.salva(
            -1,
            request.form.get("tmdb"),
            request.form.get("imdb"),
            request.form.get("titulo_original"),
            request.form.get("titulo_traduzido"),
            request.form.get("pagina"),
            request.form.get("pasta"),
            request.form.get("data_release"),
            request.form.get("link_imagem"),
            request.form.get("sinopse"),
            request.form.get("cores")
        )
        return redirect(url_for("index"))
    return render_template("novo.html")


@app.route("/excluir/<id>", methods=["GET"])
def excluir(id):
    if request.method == "GET":
        Posters.exclui(id)
    return redirect(url_for("index"))


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
