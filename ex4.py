# EXERCÍCIO ex4.py 
# ° CONDICIONAIS (IF, ELIF, ELSE)

#EXERCÍCIO 1 
# ° positivo ou negativo
num = int(input("Digite um numero:"))
if num >= 0:
    print(f"o numero {num} é positivo")

else: 
    print(f"o numero {num} é negativo")


# ° maior ou menor de idade
idade = int(input("Digite a sua idade:"))
if idade >= 18:
    print("Você é maior de idade")
else:
    print("você é menor de idade")


# ° par ou impar
num = int(input("Digite um numero:"))
if num % 2 == 0:
    print(f"O numero {num} é par")
else:
    print(f"O numero {num} é impar")


# ° situação do aluno 
nota = float(input("Digite a nota do aluno"))

if nota >= 7:
    print(f"O aluno está aprovado com a nota {nota}")

elif 5 <= nota < 7:
    print(f"O aluno está em recuperação com a nota {nota}")

else:
    print(f"O aluno está reprovado com a note {nota}")


# ° multiplo de outro numero

num = int(input("Informe um numero:"))
divisor = int(input("Informe o numero que deseja saber se é multiplo:"))

if num % divisor == 0:
    print(f"o numero {num} é multiplo de: {divisor}")

else:
    print(f"o numero {num} não é multiplo de: {divisor}")
 

 
# ° multiplo de 3 e 5

num = int(input("informe um numero:"))
 
if num % 3 == 0 and num % 5 == 0:
    print(f"O numero {num} é multiplo de 3 e 5")
else:
    print(f"O numero {num} não é multiplo de 3 e 5")


num = int(input("Informe um numero inteiro:"))

if num % 2 == 0:
    print(f"o numero é par ")

else:
    print(f'o numero é impar')



# ° Vogal ou consoante
letra = input("Informe uma letra:")

if letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u":
    print(f"A letra informada: {letra} é uma vogal")

else:
    print(f"A letra informada: {letra} é uma consoante")

# ° Nota com conceito

nota = int(input("Informe um numero inteiro de (0 a 10):"))

if nota == 9 or 10:
    print(f"Conceito A")

elif nota == 7 or 8:
    print(f"Conceito B")

elif nota == 5 or 6:
    print(f"Conceito C")

else:
    print(f"Conceito D")








