# Exercício ex7.py
# ° Funções (def, parâmentros e retorno)

# * Por que usar funções?
# - Organizam o código em blocos com nome.
# - Reaproveitam lógica (escreve uma vez, usa várias).
# - Facilitam testar e dar manutenção.

# 1) Forma básica 

# def nome_da_funcao(param1, param2):
    # faz algo
   # return resultado  # opcional, mas MUITO importante!


# Exemplos rápidos 

def soma(a, b):
    return a + b 

total = soma(2, 3)
print(total)


# ----

def saudaçao(nome= "Mundo"):
    return f"Olá, {nome}!"

saudaçao()
saudaçao("Mirella")


# ---------

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
