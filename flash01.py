from flask import app, render_template

# Rota inicial
@app.route("/")
def hello_world():
    titulo = "Pagina Inicial"
    return render_template("index.html",titulo=titulo)

