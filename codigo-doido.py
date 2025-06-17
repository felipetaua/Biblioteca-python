# velocidade_permida = 80
# velocidade_dos_veiculos = [70, 50, 120, 160, 40, 130, 180, 150, 45, 60, 110, 120, 190, 140, 150, 30, 20, 110]

# Acima = 0
# abaixo = 0

# for v in  velocidade_dos_veiculos:
#     if v > velocidade_permida: 
#         Acima += 1
#     else:
#         abaixo += 1

# print(f"Carros acima da velocidade permitida: {Acima}")
# print(f"Carros abaixo ou igual à velocidade permitida: {abaixo}")

# media = sum(velocidade_dos_veiculos) / len(velocidade_dos_veiculos)
# print(f'media: {media:.2f}')

def analisar_velocidade(velocidade_limite):
    carros_acima_velocidade = 0
    carros_abaixo_velocidade = 0

    for velocidade_veiculo in  velocidade_dos_veiculos:
        if velocidade_veiculo > velocidade_limite: 
            carros_acima_velocidade += 1
        else:
            carros_abaixo_velocidade += 1

    return carros_acima_velocidade, carros_abaixo_velocidade # 11, 7

velocidade_limite = 80
velocidade_dos_veiculos = [70, 50, 120, 160, 40, 130, 180, 150, 45, 60, 110, 120, 190, 140, 150, 30, 20, 110]

carros_acima_velocidade, carros_abaixo_velocidade = analisar_velocidade(velocidade_limite)

print(f"Carros acima da velocidade permitida: {carros_acima_velocidade}")
print(f"Carros abaixo ou igual à velocidade permitida: {carros_abaixo_velocidade}")


def media_veiculos():
    return sum(velocidade_dos_veiculos) / len(velocidade_dos_veiculos)

print(f'media de velocidade dos veiculos: {media_veiculos():.2f}km/h')


# Separamos as funcionalidades(Divisão de Funções), pois a lógica que antes estava toda "solta" no script foi separada em duas funções com responsabilidades claras:
# analisar_velocidade(): Responsável por contar os carros acima e abaixo do limite.
# media_veiculos(): Responsável por calcular a velocidade média.
# Uso de Parâmetros e Retornos: A função analisar_velocidade agora recebe o velocidade_limite como um parâmetro e retorna os valores calculados (carros_acima_velocidade, carros_abaixo_velocidade), em vez de apenas imprimi-los na tela.

# Além de nomes de Variáveis Mais Descritivos: As variáveis foram renomeadas para serem mais claras e explícitas, seguindo boas práticas (padrão snake_case).
