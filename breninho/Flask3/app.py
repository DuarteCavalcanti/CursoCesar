from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
db = SQLAlchemy(app)


class Usuario(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        nome = db.Column(db.String(80), nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        tell = db.Column(db.String(20), unique= True, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    usuarios = Usuario.query.all()
    return render_template('login.html', usuarios=usuarios) 


@app.route('/', methods=['GET', 'POST'])
def Adicionar_nomes():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        tell = request.form['tell']
        db.session.add(Usuario(nome=nome, email=email, tell=tell))
        db.session.commit()
        return redirect('/')
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug= True)