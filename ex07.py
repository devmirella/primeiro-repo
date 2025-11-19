# Exercício ex7.py

# ° Funções (def, parâmentros e retorno)

# * Por que usar funções?
# - Organizam o código em blocos com nome.
# - Reaproveitam lógica (escreve uma vez, usa várias).
# - Facilitam testar e dar manutenção.

# 1) Forma básica 

# def nome_da_funcao(param1, param2):
    # faz algo
   # return resultado  # opcional, mas MUITO importante!, return é o que uma função faz quando termina


# Exemplos rápidos 

def soma(a, b):
    return a + b 

total = soma(2, 3)
print(total)

# -----------------

def soma(y, k):
    return y + k

print(soma(5, 3))

# ----------------

soma = lambda y, k: y * k
print(soma(5, 3))

# ----
# Texto de saudação
# Essa função Cumprimenta alguém.

def saudaçao(nome= "Mundo"):
    return f"Olá, {nome}!"

saudaçao()
saudaçao("Mirella")


# ---------
# Essa função filtra e separa números pares dentro de uma lista.

def eh_par(n):
    return n % 2 == 0 # Devolve True se o numero for "Par"

def filtrar_pares(lista):  
    pares = []  # Cria uma lista vazia
    for n in lista:  # Percorre todos os números
        if eh_par(n):  # usa a outra função para decidir, eh_par(), passando o número atual (n) como argumento.
            pares.append(n)  # adicona o número se for par
    return pares   # devolve a lista final com pares

# Chamando e mostrando o retorno
resultado = filtrar_pares([1, 2, 3, 4, 5, 6])
print(resultado)


# ---------
# Essa função lê um texto, conta quantas vezes cada palavra aparece, e devolve as mais repetidas.

def top_palavras(texto, k=3): # Cria uma função com dois parâmetros: o texto e quantas palavras mostrar
    texto = texto.lower() # Coloca tudo em minúsculas pra não contar
    palavras = texto.split() # Divide o texto nos espaços e cria uma lista
    cont = {}   # Cria um um Dicionário, vai gauradar a conatagem de cada palavra
    for p in palavras : # Laço, passa por  cada palavra
        cont[p] = cont.get(p, 0) + 1 # Conta, se a palavra já existir, soma 1, se não, começa em 1

    ordenado = sorted(cont.items(), key=lambda x: x[1], reverse=True) # Ordena, coloca as palavras da mais repetida pra menos
    return ordenado[:k]  # Retorna o resultado, Devolve as 'K' palavras mais frequentes


# 1) Escreva uma função que retorne True se (n) for par

def eh_par(n):
    return n % 2 == 0
def filtrar_pares(lista):
    pares = []
    for n in lista:
        if eh_par(n):
            pares.append(n)
    return pares

resultado = filtrar_pares([1, 3, 5, 6, 8, 13, 22])
print(resultado)



def eh_par(numero):
    return numero % 2 == 0

def filtar_pares(lista):
    pares = []
    for numero in lista:
        if eh_par(numero):
            pares.append(numero)
    return pares

try:

    numero = int(input("Informe um número para descobrir se é par"))
    if eh_par(numero):
        print(f"{numero} é par!")

    else: 
        print(f"{numero} não é par!")

except ValueError:
        
        print("Erro: Você não digitou um número válido!")


def eh_par(n): # Cria uma função chamada eh_par que recebe um número n.
    if n % 2 == 0: # Usa o modolo % pata ver se há resto na divisão por 2. Se o resto for 0, é par
        return True # Retorna True se for par.
    else: # Caso contrario
        return False # Retorna False



def eh_par(n):
    if n % 2 == 0:
        return True
    else:
        return False


# Programa principal
numero = int(input("Digite um número: "))

if eh_par(numero):
    print(f"{numero} é par!")
else:
    print(f"{numero} é ímpar!")


# 2) Receba uma lista de números e retorne a media

soma = 0
contador = 0
lista = []


def lista_numero (lista): # recebe a lista
    global soma, contador # permite usar as variáveis de fora

    if not lista     # se a lista não estiver vazia
         return 0    # Se a lista estiver vazia, retorne o número 0

    for numero in lista: # percorrer cada número dentro da lista
        soma += numero 
        contador += 1
        
    media = soma / contador 
    return media 

        

    while True:
        numero = input("innforme um numero, ou 'ok' para sair").lower() # leio o que o usuário digitou como texto, vejo se é “ok” → se for, paro, senão, transformo em número e adiciono na lista.


        if numero == 'OK':  # Verifica se o usuário deseja sair
            break 

        else:
            numero = int(numero) # Transforma o texto em número
            lista.append(numero) # adiciona a lista
        
print(lista_numero(lista)) # chama a função e mostra o resultado




# 3) Retorne o fatorial de (n)

def fatorial(n):
    if n == 0:
        return 1

    resultado = 1

    for i in range(1, n + 1): # # Cria uma variável 'i' que vai um valor diferente a cada volta do laço, range (1, n + 1) gera uma sequencia de números de 1 até 'n' (0 +1 pq python para antes o último número).
        resultado *= i

    return resultado 

n = int(input("informe um numero para calcular o fatorial"))

print(fatorial(n))



# 4) Saudação

def saudaçao(nome= "Mundo"):
    return f"Olá, {nome}!"
    
    
print(saudaçao())


# 5) contador (Retorne quantas vogais existem no texto)

def palavras_texto(texto):
    texto = texto.lower()
 
    contador = 0

    for letra in texto:
        if letra in "aeiou":
            contador += 1

    return contador

texto = input("informe um texto:")
print(palavras_texto(texto))




# 6) segundo_maior(lista)

def segundo_maior(lista):
    lista = list(set(lista)) # set(lista) -> transforma a lista num conjunto(sem repetições), set é um conjunto, ele não guarda valores repetidos
    if len(lista) < 2: # Se depois de tirar as duplicatas, sobrou menos 2, então não existe, segundo maior numero:
        return None # Nesse caso, devolve None e para aqui
    lista = sorted(lista) # Coloco os números em ordem crescente
    return lista[-2] # A posição -1 é o ultimo item, e -2 é o peenúltimo, retorno esse número, que é o segundo maior da lista
print(segundo_maior([5, 2, 9, 4, 9]))
        
# ------------------------------

def segundo(lista):
    lista = list(set(lista))
    if len(lista) - 2:
        return None

    lista = sorted(lista)
    return lista[-2]

print(segundo([9, 9]))


def soma(y, k):
    return y + k

print(soma(5, 3))


soma = lambda y, k: y * k
print(soma(5, 3))