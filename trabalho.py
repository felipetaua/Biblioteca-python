compras = []


compras.append("Arroz")
compras.append("Feijão")

print(compras)

# O código não era claro, voce não voce não conseguia indentificar sua funcionalidade
# criamos uma função adicionar produto para conseguirmos adicionar produtos, e se precisar adicionar novas funcionalidade conseguimos direto na função
# foram troca de nome variáveis, criamos um função separada


produtos = [] 

def adicionar_produto(nome):
    produtos.append(nome)
    print(f"Produto '{nome}' adicionado com sucesso!")

adicionar_produto("Maçã")
adicionar_produto("Banana")

print(produtos)