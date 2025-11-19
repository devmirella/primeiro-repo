#EXERCICIO 1 - VARIÁVEIS SIMPLES

# VARIÁVEL SIMPLES COM SEU NOME
nome = 'mirella' 
print(nome)


# VARIÁVEL SIMPLES COM SUA IDADE
idade = 28
print(idade)

# VARIÁVEL SIMPLES COM SEU PESO
peso = 56
print(peso)
# peso = "56kg" -> dessa forma o peso vira uma string
# print(peso) -> dessa forma o peso vira uma string
# peso = 56
# print(peso, "kg") -> dessa forma o peso vira uma string
# peso = 56
# print(f'{peso}kg') -> dessa forma o peso vira uma string

# VARIÁVEL COM SUA ALTURA 
altura = 1.59 
print(altura)



print('meu nome é,', nome, "eu tenho,", idade, "anos de idade,", "tenho", altura, "de altura e peso", peso,"kg.")


#EXERCICIO 2 - MOSTRE OS VALORES NO CONSOLE

print("Meu nome é:", nome)
print("Minha idade é:", idade)
print("Meu peso é:", peso, 'kg')
print("Minha altura é:", altura, 'm')


# EXERCICIO 3 -  FAÇA CONTA COM AS VARIÁVEIS

idade = 28
idade_ano_que_vem =  idade + 1 
print('Minha idade ano que vem será:', idade_ano_que_vem)

peso =  56
peso_mais_cinco = peso + 5
print("Meu peso mais cinco quilos será:", peso_mais_cinco,"kg")

# Um meedico prescreveu para ser infundido 30gts por minuto em 500ml de soro fisiológico,
#\n quanto ml sera infundido em 5hrs?
soro_fisiologico = 500
gotas_por_min = 30
ml_h = gotas_por_min * 3 
tempo_de_infusão = soro_fisiologico / ml_h
print("o tempo de infusão será de:", tempo_de_infusão,"hrs.")

print(f"O tempo de infusão será de: {tempo_de_infusão:.2f} hrs.")


# CONTINUAÇÃO DO EXERCICIO 3 - CALCULE O SEU IMC

peso = 56
altura = 1.59
IMC = peso / (altura * altura) # A fórmula do IMC é peso dividido pela altura ao quadrado ou seja, altura: 1.59 x 1.59 e o resultado dividido pelo peso: 56
print('Meu IMC é:', IMC)
print(f"Meu IMC é: {IMC:.2f}","kg")


peso = 70
altura = 1.59
IMC = peso / (altura * altura)
print(f"Meu IMC é: {IMC:.2f}kg")

print(f"Meu IMC é: {peso / (altura * altura):.2f}kg.")


# EXERCICIO 4 - CRIE UMA FRASE JUNTANDO VARIÁVEIS E TEXTOS

print(f"Meu nome é: {nome} \nidade: {idade}anos \npeso: {peso}kg \altura: {altura} IMC: {IMC:.2f} ")


print(f"Meu nome é Mirella, tenho 1.59 de altura, peso 56kg, meu IMC é {56 / (1.59 * 1.59):.2f}")
