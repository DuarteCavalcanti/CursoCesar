from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def idade():
    return render_template('idade.html')

try:
    idade = int(idade_str)
except ValueError:
    return "Erro! por favor digite novamente"

if idade >= 18:
    return render_template('resultado.html', idade=idade)

if idade <= 18:
    return render_template('menor18.html', idade=idade)

else:
    return render_template('nada.html', idade=idade)


if __name__  == '__main__':
    app.run(debug=True)