# def getFeedback (nota):
#     if nota >= 90:
#         feedback = "Excelente!"
#     elif nota >= 80:
#         feedback = "Muito bom!"
#     elif nota >= 60:
#         feedback = "Bom!"
#     else:
#         feedback = "Ruim!"
#     return feedback


# print(getFeedback(80))


def getFeedback (nota):
    if nota >= 90: return "Excelente!"
    if nota >= 80: return "Muito bom!"
    if nota >= 60: return "Bom!"
    if nota >= 60: return "Média!"
    return "Ruim!"

print(getFeedback(80))