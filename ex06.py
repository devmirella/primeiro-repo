
# Exercício ex6.py

# ° Listas, String e Dicionários


lista = [1, 2, 3, 4]
print("Lista                ->", lista)


# testando "in"
print("2 in Lista           ->", 2 in lista)
print("5 in Lista           ->", 5 in lista)


# Testando "not in"
print("2 not in Lista       ->", 2 not in lista)
print("5 not in Lista       ->", 5 not in lista)


# outros exemplos com string.

palavra = "casa"
print("\nPalavra:", palavra)
print("'a' in palavra       ->", 'a' in palavra)
print("'z' not in palavra   ->", 'z' not in palavra)
 
for palavra in palavra:
    print(palavra)


# -----------

palavra = ['casa', 'carro', 'musica', 'arte']
print(palavra)

for i in palavra:
    print(i)
          
        
# -----------

            # class list
# Lista é uma coleção ordenada e mutável. Permite membros duplicados.

# index:   0        1        2         3
lista = ['casa', 'carro', 'musica', 'arte']
print(lista)
print(lista[3])

print(type(lista))


# -----------

            # class tuple
# Tupla é uma coleção ordenada e imútavel. Permite membros duplicados.

# index:   0        1   2   3
tupla = ('carro', True, 2, 3.5)
print(tupla)
print(tupla[2])

print(type(tupla))


# -----------
            # class dict
# Dicionário é uma coleção ordenada e mutável. Não permite membro duplicado

#             chave:   valor
dicionario = {"nome": "carro", "logica": True, "numero": 2, "outroNumero": 3.5}
print(dicionario)
print(dicionario["outroNumero"])

print(type(dicionario))


# ------------
            # class set
# Set é uma coleção não ordenada e não indexada, Não membro duplicado

conjunto = {"carro", True, 2, 3.5}
print(conjunto)

print(type(conjunto))


# 1) - Números ate "ok"

maior = menor = None
quantidade = soma = 0

while True:
    entrada = input("Digite um número inteiro (ou 'ok' para sair): ")

    if entrada.lower() == "ok":
        break 

    try: # Aqui o Python vai tentar executar, se alguma linha de erro (por exemplo se a entrada não for um número), o programa vai procurar um except para tratar esse erro, em vez de quebrar tudo
        numero = int(entrada) # Aqui converte o que o usuário digitou (entrada) em um número inteiro (int), se o usuário digitou algo que não é um número (tipo "abc"), vai gerar erro, por isso esta dentro do do try
        quantidade += 1 # contar quantos números  válidos o usuário digitou (ou seja "contador de quantas vezes")
        soma += numero # faz a soma dos números coom os numeros válidos que o usuário digitou (ou seja "acumulador do valor total")

        if maior is None or numero > maior: # Aqui significa que é a primeira vez que estamos atribuindo um valor para maior (maior is None),  Aqui (or numero > maior) se o número atual for maior do que o maior já salvo, ele substitui.
            maior = numero # Aqui atualiza a variável maior para guardar o o novo maior número digitado até agora.

        if menor is None or numero < menor: 
            menor = numero 
    
    except ValueError:
        print(f"Digite um número inteiro ")

if quantidade > 0:
    print(f"Quantidade: {quantidade} ")
    print(f"Soma: {soma}")
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")
    print(f"Media {soma / quantidade}")
    

# 2) - Contador de Caracteres

digitos = espaços = vogais = consoantes = 0

frase = input('Digite um frase:')

for i in frase: # esse for faz um laço que pega cada letra ou simbolo da frase
    
    if i.lower() in "aeiou": # lower() deixa minusculo (assim "A" e "a" são tratados igualmente) e in "aeiou" verifica se o caractere está dentro dessa listinha de vogais
        vogais += 1

    elif i.isalpha(): # isalpha() verifica se é letra do alfabeto.
        consoantes += 1 # Se  é letra, mas não é vogal (porque já passou pelo "if"), então é consoante.

    elif i.isdigit(): # isdigit() retorna True se o caractere for número
        digitos += 1

    elif i.isspace(): # isspace() retorna True se for espaço.
        espaços += 1

print(f"Vogais = {vogais}")
print(f"Consoantes = {consoantes}")
print(f"Digitos = {digitos}")
print(f"Espaços = {espaços}")


# 3) - Criar lista sem duplicatas 

texto = input("Números (Separados por espaço): ")
numero = texto.split() # .split() -> quebra string nos espaços
numero = [int(n) for n in texto.split()] # Transforma cada pedacinho em número (inteiros)
sem_dup = []  # sem_dup -> Lista vazia que vai guardar só os números sem repetição.

for n in numero: # Um laço que percorre cada número da lista

    if n not in sem_dup: # Aqui pergunta se o número esta na lista, sem sim "ignora" e se não, "entra".
     sem_dup.append(n) # Adiciona o numero ao final da lista

print(sem_dup)


# 4) - Número maior, segundo maior, número menor e segundo maior 

#maior = None 
#menor = None 
#segundo_maior = None 
#segundo_menor = None

maior = menor = segundo_maior = segundo_menor = None

while True:
    saida = input("\nDigite um numero inteiro ou digite 'ok' para sair")

    if saida.lower() == "ok":
        break

    try:
        numero = int(saida) # Aceita positivos e negativos
        
        # Atualiza maior e segundo_maior
        if maior is None or numero > maior:
               numero != maior   # Evita duplicado
               segundo_maior = maior 
               maior = numero 

        elif (segundo_maior is None or numero > segundo_menor) and numero != maior:
              segundo_maior = numero

        # Atualizada o menor e o segundo_menor
        if menor is None or numero < menor:
           if  numero != menor:
                segundo_menor = menor
                menor = numero 

        elif segundo_menor is None or numero < segundo_menor and numero != menor:
                segundo_menor = numero

    except ValueError:
        print(f"Digite um número valido")


if maior is None:
    print(f"Nenhum número foi digitado ")

else:
    print(f"Número maior: {maior}")

    if segundo_maior is not None:
         print(f"Segundo maior: {segundo_maior}")
    
    else:
        print(f"Não existe um segundo maior número.")

    print(f"Menor número: {menor}")

    if segundo_menor is not None:
        print(f"Segundo menor número: {segundo_menor}")

    else: 
        print(f"Não existe um segundo menor número")


 #----------------------------------------------------------------------------------


maior = menor = segundo_maior = segundo_menor = None


while True:
    saida = input(f"Digite um numero inteiro ou digite (ok) se quiser sair")

    if saida.lower() == "ok":
        break
    


    try:
        numero = int(saida)
        
        

        if maior is None or numero > maior:
           segundo_maior = maior
           maior = numero 


        elif segundo_maior is None or numero > segundo_maior:
            segundo_maior == numero


        if menor is None or numero < menor:
            segundo_menor = menor 
            menor =  numero 


        elif segundo_menor is None or numero < segundo_menor:
            segundo_menor = numero



    except ValueError:
        print(f"Digite um número valido")


if maior is None:
    print(f"Nenhum número foi digitado ")


else:
    maior == numero
    print(f"Número maior: {maior}")


    if segundo_maior is not None:
         print(f"Segundo maior: {segundo_maior}")
    
    else:
        print(f"Não existe um segundo maior número:")


    print(f"Menor número: {menor}")
    if segundo_menor is not None:
        print(f"Segundo menor número: {segundo_menor}")


    else: 
        print(f"Não existe um segundo menor número")



# 5) - Leia um texto e mostre as 3 palavras mais frequentes.

texto = input("Informe Um Texto: ").lower()

palavras = texto.split() # Divide o texto em palavras
contagem = {}            # Dicionário para contar cada palavra, Cria um dicionário vazio para contar quantas vezes cada palavra aparece. A ideia é ficar assim: {"python": 3, "é": 2, "legal": 1}.


# Conta as ocorrências 

for p in palavras:
    if p in contagem:
        contagem[p] += 1
    
    else:
        contagem[p] = 1

mais_frequentes = sorted(contagem.items(), key=lambda x: x[1], reverse=True)


print("Top 3 palavras mais frequentes: ")
for palavra, freq in mais_frequentes[:3]:
    print(f"{palavra}: {freq} vezes")


# Ordenar números

numeros = [5, 2, 9, 1]

ordenados = sorted(numeros)                     # ordem crescente
print(ordenados)

ordenados_desc = sorted(numeros, reverse=True)  # ordem decrescente
print(ordenados_desc)

        
# Ordenar tuplas pelo primeiro elemento

dados = [("b", 3), ("a", 5), ("c", 1)]

resultado = sorted(dados)                       # usa a letra (primeiro elemento) para ordenar
print(resultado)

# ------------------------------------------

dados = [("b", 3), ("a", 5), ("c", 1)]

resultado = sorted(dados)
print(resultado)

resultado_reverso  = sorted(dados, reverse=True)
print(resultado_reverso)


# Ordenar tuplas pelo segundo elemento (com key=)

dados = [("b", 3), ("a", 5), ("c", 1)]

resultado = sorted(dados, key=lambda x: x[1])
print(resultado)


contagem = {
    "python": 3,
    "é": 2,
    "legal": 1
}

ordenado = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
print(ordenado)


# Ordenar nomes de pessoas 

nomes = ["Mirella", "Ana", "João", "Bruno"]

alfabetica = sorted(nomes)
print(alfabetica)

# Ordem alfabética inversa (z - A)

nomes = ["Mirella", "Ana", "João", "Bruno"]

alfabetica = sorted(nomes, reverse=True)
print(alfabetica)


# Ordenar números decimais

valores = [4.5, 2.1, 9.8, 3.3]

crescente = sorted(valores)
print(crescente)


# Ordem Decrescente 

valores = [4.5, 2.1, 9.8, 3.3]

decrescente = sorted(valores, reverse=True)
print(decrescente)


# Ordenar lista de tuplas por nomes 

Lista = [("Carlos", 7.5), ("Ana", 8.9), ("Bruna", 6.2)]

nome = sorted(lista)
print(nome)


# Ordenar lista de tuplas pela nota (com key)

lista = [("Carlos", 7.5), ("Ana", 8.9), ("Bruna", 6.2)]

nome = sorted(lista, key=lambda y: y[1] )
print(nome)


# lista com valores, usando enumerate

valores = []
valores.append(6)
valores.append(30)
valores.append(1)
valores.append(8)

for c, i in enumerate(valores):
    
    print(f"na posição {c} encontrei o valor {i}")
    print(f"Cheguei ao final da lista.")



# lista com valores (0, 5)

valores = list()
for cont in range(0, 5):
    valores.append(int(input('informe um numero:'))) #aquivai ler quantos numero eu colocar na linha acima, range(0, 5) que no caso aqui é 5 vezes, e vai mostrar os numeros e a posição de cada um.


# Faça uma lista que peça 5 numeros

print('faça uma lista que peça 5 numeros')

lista = []
maior = 0
menor = float('inf')

for c in range(5):
    n = int(input('informe um numero:'))

    lista.append(n)
    print(f'na posição {c} tem o numero {n}')

    if n > maior:
        maior = n 

    if n < menor:
        menor = n 

print(f'o maior numero {maior}, na posição:..', end=' ')
for c, valor in enumerate(lista):
    if valor == maior:
        print(c, end=' ')

print(f'o menor numero {menor}, na posição:')
for c, valor in enumerate(lista):
    if valor == menor:
        print(c, end=' ')