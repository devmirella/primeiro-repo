# Exercício ex8.py
# ° TRATAMENTO DE ERROS (try/ except finally)

# Conceito: Quando algo dá errado no código, o python interrompe a execução e mostra um erro.
# Bloco try/except permite que tratemos o erro, sem encerrar o programa

# try:
#     código que pode gerrar erro
# except:
#     O que fazer se de erro

#       Exemplo

try:
    numero = int(input("Digite um numero: "))
    resultado = 10 / numero
    print("resultado:", resultado)

except:
    print("Não é possivel dividir por zero!")