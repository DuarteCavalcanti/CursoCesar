from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo Aluno


class Aluno(db.Model):
    cpf = db.Column(db.String(14), primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)


with app.app_context():
    db.create_all()

# Rota para exibir a página de login


@app.route('/login', methods=['GET', 'POST'])
def login():
    alunos = Aluno.query.all()
    return render_template('login.html', alunos=alunos)

# Rota para cadastrar um aluno


# Rota para exibir a página de cadastro
@app.route('/cadastro', methods=['GET'])
def exibir_cadastro():
    return render_template('cadastro.html')

# Rota para cadastrar um aluno


@app.route('/cadastro', methods=['POST'])
def cadastrar():
    cpf = request.form['cpf']
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']

    # Verifica se o CPF já existe
    if Aluno.query.filter_by(cpf=cpf).first():
        return "Erro: CPF já cadastrado!", 400

    novo_aluno = Aluno(cpf=cpf, nome=nome, email=email, telefone=telefone)
    db.session.add(novo_aluno)
    db.session.commit()

    return redirect(url_for('login'))


# Executar o servidor
if __name__ == '__main__':
    app.run(debug=True)
