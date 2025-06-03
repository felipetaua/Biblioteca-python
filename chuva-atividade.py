# ex2

dias_chuva = [1, 0, 1, 0, 1, 1, 0]

acidentes = [5, 2, 6, 3, 7, 6, 2]

dias = list(range(len(dias_chuva)))

com_chuva = [a for d, a in zip(dias_chuva, acidentes) if d ==1]

sem_chuva = [a for d, a in zip(dias_chuva, acidentes) if d ==0]


print(f"Média de acidentes com chuva: {sum(com_chuva)/len(com_chuva):.2f}")
print(f"Média de acidentes sem chuva: {sum(sem_chuva)/len(sem_chuva):.2f}")

# sum() soma dos valores da lista
# zip junta os nummero em pares
# for laço de repetição
# len numero de elementos na lista 
# .2f formata o número com duas casas decimais

