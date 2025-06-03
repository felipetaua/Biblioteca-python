notas = [8.5, 9.0, 9.2, 9.7]

media = sum(notas) / len(notas)

print(f"A média do aluno é {media:.2f}")

if media >= 8.4 :
    print("Indução: O aluno provavelmente manterá um bom desempenho")
else :
    print("Indução: O desempenho pode melhorar ou piorar")