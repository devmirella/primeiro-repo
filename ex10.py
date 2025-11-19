# Exercício ex10.py

# ° Funções em Python
# tipo de funções:

# 1) Sem parâmentros

def boas_vindas():    
    print("Olá, sejam bem vindos ao ex10.py ")
boas_vindas()


# 2) Com parâmentros

def apresentar(nome):
    print(f"Prazer em te ver, {nome}!")
apresentar("João")


# 3) Com retorno (return)

def soma(a,b):
    return a + b
resultado = soma (3, 7)
print("A soma é", resultado)

# ----+------

def soma(y, x):
    return y  * x
print(soma(7,5))


# 4) Mostrar o dobro
def most_dobro():
    numero = int(input("Digite um numero: "))
    dobro = numero * 2
    print(f"O dobro de {numero} é {dobro} ")
most_dobro()

#----+------

def cal_dobro(numero): # * Se a função tem parâmentro, o valor vem de fora.
    return numero * 2
numero = int(input("Digite o valor:"))
print(cal_dobro(numero))

# -------+---------

def cal_dobro(): # * Se a função não tem parâmentro, pode usar input dentro dela.
    numero = int(input("Digite o valor"))
    return numero * 2
print(cal_dobro())



