from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"Biblioteca Online.\nSeja bem-vindo!"}

@app.route("/sobre")
def status():
    return {"Somos uma Biblioteca online!\nFaça seu cadastro e começe agora mesmo a ler livros!"}

@app.route("/cadastro-livro")
def cadastro_livro():
    return "Cadastro de Livros!"

@app.route("/livros")
def livros():
    return "Lista de Livros cadastrados!"

@app.route("/cadastro-autores")
def cadastro_autores():
    return "Cadastro de Autores!"

@app.route("/autores")
def autores():
    return "Lista de Autores cadastrados!"

@app.route("/contato")
def contato():
    return "Entre em contato!"

if __name__ == "__main__":
    app.run(debug=True)
