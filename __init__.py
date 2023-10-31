from flask import Flask, request,flash, render_template, redirect, Request
from  flask_mail import Mail, Message
from config import email, senha

app = Flask(__name__) # Inicializa a aplicação
app.secret_key = "meuconsierge"

mail_settings = {
   "MAIL_SERVER":'smtp.gmail.com',
   "MAIL_PORT": 465,
   "MAIL_USE_TLS": False,
   "Mail_USE_SSL": True,
   "Mail_USERNAME": email,
   "Mail_PASSWORD": senha,
}

app.config.update(mail_settings)
mail = Mail(app)

class Contato:
   def __init__(self, nome, email, mensagem):
      self.nome = nome, 
      self.email = email,
      self.mensagem = mensagem

@app.route('/') # Cria uma rota
def index():
  return render_template("index.html")

@app.route('/send', methods=['GET','POST'])

def send():
    if request.method =='POST':
        formContato = Contato(
            request.form["nome"],
            request.form["email"],
            request.form["mensagem"]
        )
        
        msg = Message(
            subject= "Contato de f{formContato.nome} em seu Portfólio",
            sender= app.config.get("MAIL_USERNAME"),
            recipients= ['rivaz.claudio@gmail.com', app.config.get("MAIL_USERNAME")],
            body = f''' 

            {formContato.nome} te enviou uma mensagem:

            {formContato.mensagem}

            '''
        )
        mail.send(msg)
        flash("Mensagem Enviada Com Sucesso")
    return redirect ('/')

if __name__ == '__main__':
      app.run(debug=True)