# média de vendas

vendas = [120, 130, 125, 118, 140, 150, 145]

media = sum(vendas) / len(vendas)

print(f"Vendas médias: {media:.2f}")
print("Previsão: a próxima venda será aproximadamente", round(media))


# sum(vendas) soma todos os valores da lista vendas.
# len(vendas) conta quantos itens há na lista
# A divisão sum(vendas) / len(vendas) calcula a média aritiméticas dos valores da lista
# O resultado é armazenado na variável na variável média