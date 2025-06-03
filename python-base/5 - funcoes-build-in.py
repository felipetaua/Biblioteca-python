# 📌 Funções Built-in
# ➤ São funções nativas da linguagem Python.
# ➤ Estão sempre disponíveis sem precisar importar nada.
# ➤ Lista completa: https://docs.python.org/3/library/functions.html

# abs() → Retorna o valor absoluto (ignora o sinal)
print(abs(-9))  # Resultado: 9

# min() → Retorna o menor valor de uma sequência
menor_preco = min(8, 3, 5, 6)
print(menor_preco)  # Resultado: 3

# max() → Retorna o maior valor de uma sequência
maior_preco = max(8, 3, 5, 6)
print(maior_preco)  # Resultado: 8

# sum() → Soma os valores de uma sequência
soma_total = sum([1, 2, 3])
print(soma_total)  # Resultado: 6

# pow() → Potenciação
# Mesma coisa que usar **
print(2 ** 3)      # Resultado: 8
print(pow(2, 3))   # Resultado: 8

# print() → Exibe valores na saída (terminal)
print("Olá, esse é meu texto")  # Resultado: Olá, esse é meu texto
print(soma_total)               # Resultado: 6

# input() → Lê um valor digitado pelo usuário (sempre retorna uma string)
nome = input("Qual seu nome? ")  # Aparece: Qual seu nome? (aguarda digitação)
print(nome)                       # Mostra o que foi digitado

#O input() sempre retorna uma string, mesmo que você digite um número. Se quiser fazer cálculo, precisa converter:
#Ex.: idade = int(input("Qual sua idade? "))


# help() → Mostra a documentação de uma função diretamente no terminal
help(max)  # Mostra como funciona a função max()
help(sum)  # Mostra como funciona a função sum()

