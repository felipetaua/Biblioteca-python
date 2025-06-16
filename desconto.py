def calcula_preco_com_desconto(preco, desconto):
    if desconto > 0:
        return preco - (preco * desconto / 100)
    else:
        return preco
    
print(calcula_preco_com_desconto(200, 10))
print(calcula_preco_com_desconto(200, 00))


