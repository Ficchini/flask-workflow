from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"Biblioteca Online.\nSeja bem-vindo!"}

@app.route("/sobre")
def status():
    return {"Somos uma Biblioteca online!\nFaça seu cadastro e começe agora mesmo a ler livros!"}

if __name__ == "__main__":
    app.run(debug=True)
