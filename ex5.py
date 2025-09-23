# Exercício ex5.py
# ° Estruturas de Repetição

# ° Contagem com For
num = int(input("informe um numero:"))

for i in range(1, num + 1):
    print(i)


# ° Tabuada com While 
num1 = int(input("informe um numero:"))

i = 1
while i <= 10:
    print(f" {num1} x {i} = {num1 * i }")
    i += 1

    
# ° Soma de Números
soma = 0

while True:
    num = int(input("informe um numero:"))
    if num == 0:
        break
    soma += num 
print(f"A soma do numero informado: {soma}")



# ° Números Pares 
numero = int(input("informe um numero:"))

for i in range(2,       numero + 1,   2): # começa em 2, vai até numero, pulando de 2 em 2.
#              inicio,  fim,          passo.
    print(i)


# ° Contar de 1 a 10:
for i in range(1, 11):
    print(i)


# ° Contar de 0 a 20 de 5 em 5
for i in range(0, 21, 5):
    print(i)


# ° Contar de tras pra frente de 10 a 1
for i in range(10, 0 -1):
    print(i)

    
# ° Fatorial 
num = int(input("Digite um numero para calcular o fatorial: "))
fatorial = 1

for i in range(1, num +1):
    fatorial *= i
print(f"O fatorial de {num} é {fatorial}")


# ° Media de Notas
quantidade = int(input("Quantas notas você deseja digitar? "))
soma = 0

for i in range(quantidade):
    nota = float(input(f"Digite a nota: {i + 1}"))
    soma += nota 

media = soma / quantidade
print(f"A media é {media:.2f}")


# ° Advinhação 
import random

segredo = random.randint(1, 10)
tentativa = 0

while True:
    palpite = int(input("Advinhe um numero (ente 1 a 10) "))
    tentaiva += 1

    if palpite == segredo:
        print(f"Parabéns, acertou em {tentaiva}")


# ° Jogo de Advinhação

    import random

    segredo = random.randint(1, 10)
    tentativa = 0

    while True:
        palpite = int(input("Adivinhe o número (1 a 10): ou digite 50 para sair."))
        tentativa += 1

        if palpite == segredo:
            print(f"Parabéns! Você acertou {tentativa} tentativas ")
            break 

        elif palpite < segredo:
            print(f"O número é maior.")
    

        else: 
            print(f"O número é menor.")