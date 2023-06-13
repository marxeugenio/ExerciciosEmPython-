from flask import Flask 
from flask import redirect
from flask import request

# Cria uma instância do Flask
app = Flask(__name__)

# Rota inicial
@app.route("/")
def hello_world():
    return"Olá, Mundo! "

# Rota para exibir um nome específico
@app.route("/nome/<string:nome>")
def exibir_nome(nome):
    return f"Olá,{nome}!"

# Rota para exibir um número
@app.route("/numero/<int:num>")
def exibir_numero(num):
    return f"O número é {num}"

# Rota para lidar com métodos POST e GET
@app.route("/formulario", methods=["GET","POST"])
def formulario():
    if request.method == "POST":
        return "Você enviou o formulário"
    else:
        return "Este é um formulário GET"
    
# Rota para redirecionar para outra página
@app.route("/redirecionar")
def redirecionar():
    return redirect("/")

# Rota para lidar com erros 404
@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return "Pagina não encontrada", 404

# Executa o aplicativo Flask
if __name__ == "__main__":
    app.run()