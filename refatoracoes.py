# x = 5
# value = input("Enter a number: ")
# y = int(value)
# if x < y:
#     print(f"{x} é menor que {y}")
# elif x == y:
#     print(f"{x} é igual a {y}")
# else:
#     print(f"{x} é maior que {y}")


x = 5; y = int(input("Enter a number:"))
equality = "é igual a " if x == y else "é menor que" if x < y else "é maior que"
print(f"{x} {equality} {y}")

# Problema dessa refatoração é que ela é muito complexa e não é facil de ententer, logo melhor utilizar a outra versão