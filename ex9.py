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
