with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Primeira linha de dados no arquivo TXT.\n")
    arquivo.write("Segunda linha armazenada com sucesso!\n")

with open("dados.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo TXT:")
    print(conteudo)