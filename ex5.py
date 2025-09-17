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

numero = int(input("informe um numero para calcular o fatorial:"))

if numero < 0:
    print("Não é possível calcular fatorial de número negativo.")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"O fatorial de {numero} é {fatorial}")