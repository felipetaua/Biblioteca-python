# Calcule a soma dos numeros do 10 ao 14

print(10 + 11 + 12 + 13 + 14)
# 60

somaNum = sum([10, 11, 12, 13, 14])
print("A soma dos numeros é", somaNum)
# A soma dos numeros é 60


# Calcule a média entre os numeros 10, 15 e 20

media = (10 + 15 + 20) / 3
print("A média dessas notas são", media)
# A média dessa lista é 15.0


# Peça para o usuario digitar duas notas de zero a dez e os pesos das notas
# e calcule a média ponderada entre elas. 
# Exemplo: media = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)

# lembrando que a soma dos pesos precisa ser dez

# Como o campo input retorna str (texto)
# e para conseguir utilizar os operadores precisamos que os valores sejam int ou float,
# precisamos converter.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

peso1 = float(input("Digite o peso da primeira nota: "))
peso2 = float(input("Digite o peso da segunda nota: "))

media = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)

print(f'Sua média é: {media}')
# Exemplo:
# Digite a primeira nota:4
# Digite a segunda nota:9
# Digite o peso da primeira nota:10
# Digite o peso da segunda nota:10
# Sua média é: 6.5


notaA = float(input("Digite a primeira nota: "))
notaB = float(input("Digite a segunda nota: "))

pesoA = float(input("Digite o peso da primeira nota: "))
pesoB = float(input("Digite o peso da segunda nota: "))

mediaNota = (notaA * pesoA + notaB * pesoB) / (pesoA + pesoB)

print(f'Sua média é: {mediaNota:.2f}')
# Exemplo:
# Digite a primeira nota:10
# Digite a segunda nota:10
# Digite o peso da primeira nota:10
# Digite o peso da segunda nota:5
# Sua média é: 10.0


# Qual o menor preço dessa lista? Preços: R$100.20, R$34.90, R$31.50, R$18.95

menorPreco = min(100.20, 34.90, 31.50, 18.95)
print(menorPreco)
# 18.95


# Avalie se o número digitado pelo usuário é par ou ímpar.
# Se for par a saída deve mostrar True, se ímpar deverá mostrar False

numeroUser = int(input("Digite um numero: "))

if (numeroUser % 2 == 0):
    print("True")
else:
    print("False")
# Exemplo:
# Digite um numero: 2
# True


# Verifique se o menor preço dessa lista é menor que R$20,00
# Preços: R$100.20, R$34.90, R$31.50, R$18.95

minPreco = min(100.20, 34.90, 31.50, 18.95)

if (minPreco < 20):
    print("True")
else:
    print("False")
# Resultado: True


# Faça um programa que converta a temperatura em graus Fahrenheit fornecida
# pelo usuário em graus Celsius.
# Fórmula: celcius = (5/9) * (fahrenheit - 32)

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

celcius = (5/9) * (fahrenheit - 32)

print(f'A temperatura em celcius é: {celcius:.2f}')
# Exemplo:
# Digite a temperatura em Fahrenheit: 32
# A temperatura em celcius é: 0.0
