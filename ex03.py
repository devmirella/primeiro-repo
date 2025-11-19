# EXERCÍCIO ex3.py - 
# °INPUT E INT DO USUÁRIO

#PEDINDO DADOS DO USUÁRIO

nome = input("QUAL É O SEU NOME?")
idade = int(input("QUAL É O SEU IDADE? "))
cidade = input("QUAL É A SUA CIDADE?")

print(f"Meu nome é: {nome}")
print(f"Minha idade é:, {idade}anos")
print(f"Minha cidade é: {cidade}")



# EXERCÍCIO 1 
# ° pergunte o nome e a idade

nome = input("Qual é o seu nome?")
idade = int(input("Qual sua idade?"))

print(f"Olá, {nome}! você tem {idade}anos")


# EXERCÍCIO 2 

# ° pergunte o nome e a cidade
nome = input("Qual é o seu nome?")
print(f"Prazer em te conhecer, {nome}")
cidade = input("Você mora em qual cidade?")
estado = input(f"E em qual estado do pais que a cidade de {cidade} fica?")
print(f'Que legal, {nome}! Eu também moro em {cidade} - {estado}!')


# EXERCÍCIO 3 

# ° peça dois numeros e mostre a soma entre eles
num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero:"))
print(f"{num1} + {num2} = {num1 + num2}")
# OBS: int(float()) -> transforma o valor em float e depois em int, assim o usuario pode digitar numeros com virgula ou ponto.


# *Continuação do EXERCICIO 3 
# ° soma
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero:"))
resultado =  (num1 * num2) / num3
print(f" Resultado = {resultado}")


# *Continuação
# ° subtração 
num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero:"))
print(f" {num1} - {num2} = {num1 - num2}")


# *Continuação
# ° divisão 
num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero:"))
divisão = num1 % num2 
print(f" O resto da divisão entre {num1} e {num2} é: {divisão:.2f}")
# OBS: :.2f -> limita o numero de casas decimais para 2.


