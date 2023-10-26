from flask import Flask, request, render_template, redirect, Request


app = Flask(__name__) # Inicializa a aplicação

@app.route('/') # Cria uma rota
def index():
  return render_template("index.html")

@app.route('/terapeutas') # Cria uma rota
def terapeutas():
  return render_template("terapeutas.html")

@app.route('/minhaagenda') # Cria uma rota
def minha_agenda():
  return render_template("agenda.html")


if __name__ == '__main__':
      app.run(debug=True)