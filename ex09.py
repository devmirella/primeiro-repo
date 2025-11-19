# Exercício ex9.py
# ° Manipulação de arquivos (Leitura e Escrita)


# 1) Olá mundo!
with open("teste.txt", "w", encoding="utf-8") as f:
    f.write("Olá mundo!\n")
    f.write("Este é um teste de escrita em arquivo.\n")

with open("teste.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()
    print("Conteúdo do arquivo: ")
    print(conteudo)


# --------------------------------------------------

with open ("dados.txt", "w") as arquivos:
    arquivos.write("Olá mundo!")

with open ("dados.txt", "r") as arquivos:
    conteudo = arquivos.read()
    print(conteudo)



# 2) gravação
with open("nomes.txt", "w") as arquivos:
    arquivos.write("luana\n")
    arquivos.write("Jessica\n")
    arquivos.write("João\n")

with open("nomes.txt", "r") as arquivos:
    conteudo = arquivos.read()
    print("Conteúdo do arquivos: ")
    print(conteudo)


# 3) cadastro de nomes
with open("nomes.txt", "w") as arquivo:
    while True:
        nomes = input("Digite um nome (ou 'sair' para encerrar): ")
        if nomes.lower() == "sair":
            break 
        arquivo.write(nomes + "\n")

print("\n--- Nomes salvos com sucesso! ---\n")

with open("nomes.txt", "r") as arquivo:
    print("Lista de nomes gravados: ")
    print(arquivo.read())


# 4) Manipulação de arquivos

frase = input("Informe uma frase: ")
with open("frase.txt", "w") as arquivo:
    arquivo.write(frase)

with open("frase.txt", "r") as arquivo:
    print("Frase informada")
    print(arquivo.read())


# 5) Use o modo "a" para continuar gravando

with open("texto.txt", "a", encoding="utf-8" ) as f:
    f.write("Boa noite!")
    f.write("Esta uma linda noite!")
    f.write("As estrelas, assim como arte, me fazem sorrir.")

with open("texto.txt", "r", encoding="utf-8" ) as f:
    conteudo = f.read()
    print("Conteudo gravado:")
    print(conteudo)


# outra forma de fazer 

with open("tex.txt", "a", encoding="utf-8" ) as s:
    s.write(input("informe uma frase")+ "\n")
    print("Texto adicionado!" )

with open("tex.txt", "r", encoding="utf-8" ) as s:
    conteudo = s.read()
    print(conteudo)


# outra forma de fazer 

with open("ttx.txt", "a", encoding="utf-8") as p:
    while True:
        texto = input("Informe a frase ou texto que desejar ('sair' para finalizar) ")

        if texto.lower( )== "sair":
            break 

        p.write(texto + "\n")

    print("Textos ou frases adicionadas! ")


with open("ttx.txt", "r", encoding="utf-8" ) as p:
    conteudo = p.read()
    print(conteudo)


