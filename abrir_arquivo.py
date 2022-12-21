try:
    with open('email.txt') as arquivo:
        conteudo = arquivo.readlines()
        for linha in conteudo:
            print(linha.strip())

except FileNotFoundError:
    print('>>>> não conseguimos abrir arquivo inexistente!')


