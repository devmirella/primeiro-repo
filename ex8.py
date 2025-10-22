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


# 1) Preços e produtos

#                   Dicionario = {},   lista = []

preços_produtos = {
                    "Iphone": 5000,
                    "Ipad"  : 7000,
                    "Airpod": 2000
}

# produto = "Iphone".lower()
produto = input("Informe o nome do produto que deseja: ")

try:
    preço = preços_produtos[produto]

except:
    print("Produto não encontrado!")

else:
    print(f"Preço do {produto}: R${preço}")


#  -----------------------------------------------


produto_preço = {
                    "iphone" : 5000
                    "airpod" : 2000
                    "ipad"   : 7000
}

produto = int(input("Informe o nome do produto: ")).lower()

try:
    preço = produto_preço[preço]
    print(f"valor do {produto} e R${preço}")

except:
    print("Produto não encontrado!")


# 2) Media de notas

notas = []
c = 0
while True:
    try:
        n = int(input("Informe o numero de provas: "))
        while c < n:
            try:
                notas.append(float(input(f"Informe a {c+1}ª nota: ")))
                c += 1

            except:
                print("Informe uma nota valida:")

        break 
    except:
        print('Voce não digitou um numero inteiro válido!')
# sum(), soma os numeros da lista e len(), quantos números trm.
media = sum(notas)/len(notas)
print(f"A media das notas informadas são: {media:.1f} ")


# 3) Divisão por 0
try:
    numero = int(input(f"Informe um numero:"))
    n = 10 / numero
    print(f"Resultado: {n}")

except:
    print(f"Não é possivel dividir por 0!")


# 4) Tipos de erros especifico
try:
    nome = input(f"Informe seu nome: ")
    idade = int(input(f"Informe sua idade: "))
    print(f"Olá, {nome}, Você tem {idade} anos. ")

except:
    print(f"idade deve ser um numero inteiro!")
    
