# refatoração 
# processo de melhora de codigo existente
# modifica para deixar o codigo mais legivel

#pq refatorar: legibilidade, facilita manutenção, reduz a complexidade, evita duplicações e aumenta a qualidade

# Refatoração: modifica o código existente para melhorar sua estrutura, mantendo a funcionalidade.
# Reescrita: Criar código do zero, normalmente quando o código atual esta muito ruim ou obsoleto.

'''Código para refatorar'''


'''
    def calcular_preco_final(preco, quantidade, desconto): 
        total = preco * quantidade

        if desconto > 0:
            desconto_valor = total * desconto
            total = total - desconto_valor
        return total

    preco = 10
    quantidade = 5
    desconto = 0.1

    print("Preco final: ", calcular_preco_final(preco, quantidade, desconto))
'''

def calcular_preco_final(preco_unitario, quantidade, desconto): 
    total_bruto = preco_unitario * quantidade

    if desconto > 0:
        desconto_valor = total_bruto * (desconto / 100)
        total = total_bruto - desconto_valor
    else:
        total = total_bruto
    return total

preco_produto = 10
quantidade_produtos = 5
desconto = 10

preco_final = calcular_preco_final(preco_produto, quantidade_produtos, desconto)

print(f"Preco final: R${preco_final:.2f}")


