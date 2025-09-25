
# Exercício ex6.py
# ° Listas, String e Dicionários


# 1 - Números ate "ok"
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
    


# 2) Contador de Caracteres

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


# 3) Criar lista sem duplicatas 
texto = input("Números (Separados por espaço): ")
numero = texto.split() # .split() -> quebra string nos espaços
numero = [int(n) for n in texto.split()] # Transforma cada pedacinho em número (inteiros)
sem_dup = []  # sem_dup -> Lista vazia que vai guardar só os números sem repetição.
for n in numero: # Um laço que percorre cada número da lista
    if n not in sem_dup: # Aqui pergunta se o número esta na lista, sem sim "ignora" e se não, "entra".
     sem_dup.append(n) # Adiciona o numero ao final da lista
print(sem_dup)



lista = [1, 2, 3, 4]
print("Lista                ->", lista)

# testando "in"
print("2 in Lista           ->", 2 in lista)
print("5 in Lista           ->", 5 in lista)

# Testando "not in"
print("2 not in Lista       ->", 2 not in lista)
print("5 not in Lista       ->", 5 not in lista)

# outros exemplos com string 
palavra = "casa"
print("\nPalavra:", palavra)
print("'a' in palavra       ->", 'a' in palavra)
print("'z' not in palavra   ->", 'z' not in palavra)

