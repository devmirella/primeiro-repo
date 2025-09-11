#EXERCÍCIO 4 ex4.py - 
# ° CONDICIONAIS (IF, ELIF, ELSE)

# EXERCÍCIO 1 
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

n






