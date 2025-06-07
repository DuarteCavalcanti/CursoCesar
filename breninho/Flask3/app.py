from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
db = SQLAlchemy(app)



class Usuario(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        nome = db.Column(db.String(80), nullable=False)
        email = db.Column(db.String(120), nullable=False)
        tell = db.Column(db.String(20), nullable=False)

class Prod(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_prod = db.Column(db.String(80), nullable=False)
    preco = db.Column(db.String(120), nullable=False)
    desc = db.Column(db.String(1111 ), nullable=True)
    data_vencimento = db.Column(db.String(20), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        tell = request.form['tell']
        db.session.add(Usuario(nome=nome, email=email, tell=tell))
        db.session.commit()
        return redirect('/')
    
    usuarios = Usuario.query.all()
    return render_template('login.html', usuarios=usuarios)

@app.route('/prod', methods=['GET', 'POST'])
def gerenciar_prod(): 
    if request.method == 'POST':
        nome_prod = request.form.get('nome_prod')
        preco = request.form.get('preco')
        desc = request.form.get('desc')
        data_vencimento = request.form.get('data_vencimento')
        db.session.add(Prod(nome_prod=nome_prod, preco=preco, desc=desc, data_vencimento=data_vencimento))
        db.session.commit()
        return redirect('/prod')
  
    produtos = Prod.query.all()
    return render_template('/prod', produtos=produtos)


# @app.route('/prod.html', methods=['GET', 'POST'])
# def Adicionar_produtos():
#     if request.method == 'POST':
#         nome_prod = request.form.get('nome_prod')
#         preco = request.form.get('preco')
#         desc = request.form.get('desc')
#         db.session.add(Prod(nome_prod=nome_prod, preco=preco, desc=desc))
#         db.session.commit()
#         return redirect('/prod.html')
#     return render_template('prod.html')

if __name__ == '__main__':
    app.run(debug= True)