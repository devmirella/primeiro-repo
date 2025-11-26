# Exercício 11

# Revisão Geral 

# 1 - Pergunte o nome de usuario e cumprimente ele.

# Resposta Inicial
print("Qual seu nome?")
nome = input()
print("Olá, " + nome + "!")

# Resposta 
print("Qual seu nome?")
nome = input()
print(f'Olá, {nome}!')



# 2 - Ler idade 

# Resposta Inicial
print("Qual sua idade?")
idade = input()
print(f"Sua idade é {idade} anos.")

# Resposta 
print("Qual sua idade?")
idade = input(f"Sua idade? ")
print(f"Sua idade é {idade} anos.")



# 3 - Somar números até digitar "ok"

# Resposta Inicial
soma = 0
while True:
    print(f"Digite um número para somar ou 'ok'para sair: ")
    numero = input()
    if numero.lower() == "ok":
        break 
    soma += int(numero)
print(f"A soma dos números é {soma}")



# 4 - Encontre maior e o menor 

# Resposta Inicial 
numero = []
while True:
    entrada = input("Digite um número ou 'sair' para sair: ")
    if entrada == "sair":
        break 
    numero.append(int(entrada))
print(f"O maior número é {max(numero)} e o menor é {min(numero)}")
    


# 5 - contar caracteres em um texto

# Resposta Inicial 
print("Digite um Texto: ")
texto = input()
print(f'O texto tem {len(texto)} caracteres.')



# 6 - Criar uma pequena calculadora 


# Resposta Inicial 

num1 = int(input(f"Digite o Primeiro número:"))
num2 = int(input(f"Digite o Segundo número: "))

print("Escolha qual operação deseja:")
print("[+] Adição")
print("[-] Subtração")
print("[*] Multiplicação")
print("[/] Divisão")

operacao = input("Digite o símbolo da operação: ")

if operacao == '+':
    print(f"soma dos {num1} + {num2}: {num1 + num2} ")

elif operacao == '-':
    print(f"soma dos {num1} - {num2}: {num1 - num2} ")

elif operacao == "*":
    print(f"Soma dos {num1} * {num2}: {num1 * num2} ")

elif operacao == "/":
    print(f"Soma dos {num1} / {num2}: {num1 / num2}")
else:
     print("Operação inválida.")



# 7 - Repetir  via funções

# Resposta 
def repetir_string():
    texto = input(f"Digite um texto: ")
    vezes = int(input(f"Quantas vezes deseja repetir? "))
    print(texto * vezes)
    
repetir_string()