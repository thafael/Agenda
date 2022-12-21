try:
    with open('nomes.txt', 'a') as arquivo:
        arquivo.write('\nMessias Teixeira')
except Exception as error:
    print('Algum erro ocorreu')
    print(error)