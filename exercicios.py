# 1.	Peça ao usuário sua idade e diga se ele pode votar (idade ≥ 16).
# 2.	Solicite uma nota e classifique:
# o	Nota ≥ 9: "Excelente"
# o	Nota ≥ 7: "Bom"
# o	Nota ≥ 5: "Regular"
# o	Caso contrário: "Insuficiente"

yourAge = int(input("Insira sua idade: "))

if (yourAge >= 16) :
    print("Você pode votar")
else :
    print("você não pode votar ainda")

# input() solicita que o usuário digite um valor (idade)
# int() converte a entrada para numeros inteiros

yourNote = float(input("Insira sua idade: "))

if (yourNote >= 9 ) :
    print("Excelente")
elif (yourNote >= 7) :
    print("Bom")
elif (yourNote >= 5) :
    print("Regular")
else :
    print("Insuficiente")





