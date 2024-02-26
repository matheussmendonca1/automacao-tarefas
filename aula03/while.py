print('exemplo 1: ================\n')
i = 0
while i < 5:
    print(i, 'vezes')
    i+=1

print('exemplo 2: ================\n')
nomes = []
while True:
    nome = input('Digite um nome: ')
    nomes.append(nome)

    if(nome == 'fim'):
        break
