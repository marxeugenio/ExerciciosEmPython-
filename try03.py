try:
    arquivo = open("arquivo.txt","r")
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("Erro: arquivo não encontrado!")
finally:
    if arquivo:
        arquivo.close()