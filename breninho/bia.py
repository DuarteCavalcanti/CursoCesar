class prod:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
        
    def mostrar_detalhes(self):
        return 'Nome: {} \nPreco: {}'.format(self.nome, self.preco)
        
class eletronicos(prod):
    def __init__(self, nome, preco, marca):
        super().__init__(nome, preco)
        self.marca = marca
        
        
    def mostrar_detalhes(self):
        return '{}\n Marca{}'.format(super().mostrar_detalhes(), self.marca)
        
        
class  roupa (prod):
    def __init__(self, nome, preco, marca, cor, tipo):
        super().__init__(nome, preco)
        self.marca = marca
        self.cor = cor
        self.tipo = tipo

    def mostrar_detalhes(self):
        return '{} \nMarca: {} \nCor: {}'.format(super().mostrar_detalhes(), self.marca, self.cor)
    
    
class livro(prod):
    def __init__(self, nome, preco, autor, editora):
        super().__init__(nome, preco)
        self.autor = autor
        self.editora = editora
        
    def mostrar_detalhes(self):
        return '{} \nAutor: {} \nEditora: {}'.format(super().mostrar_detalhes(), self.autor, self.editora)
        
produtos = [
    eletronicos('Nitro 5', 5.00, 'Aceer'),
    roupa('Camisa', 22.000, 'Gucci', 'Preto', 'Gola Alta' ),
    livro('Os Sertões', 12.00, 'Helio Gutemberg', 'Instituto Silvestre LTDA'),
    roupa('Calcinha', 20.50, 'Vitoria Secrets', 'Vermelha', 'renda')
]
for produto in produtos:
    print("{}\n".format(produto.mostrar_detalhes()))