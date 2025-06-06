from flask import Flask, render_template, request

app = Flask(__name__)

prod = []

@app.route('/', methods=['GET', 'POST'])

def gerenciar_produtos():
    if request.method == 'POST':
        nome_prod = request.form.get('nome_prod')
        preco = request.form.get('preco')
        desc = request.form.get('desc')
        prod.append({'Nome': nome_prod, 'preco': preco, 'desc': desc} )
        return render_template('prod.html', prod=prod)

if __name__ == '__main__':
    app.run(debug=True)

# def gerenciar_produtos():
#     if request.method == 'POST':  # Apenas adiciona quando for POST
#         nome_prod = request.form.get('nome_prod')
#         preco = request.form.get('preco')
#         desc = request.form.get('desc')

#         if nome_prod and preco:  # Verifica se os campos obrigatórios foram preenchidos
#             prod.append({'Nome': nome_prod, 'preco': preco, 'desc': desc})

#     return render_template('prod.html', prod=prod)  # Renderiza a lista atualizada
