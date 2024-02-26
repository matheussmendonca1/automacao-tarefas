print('exemplo 1 - normal\n')
for i in range(0, 10):
    print(i, 'vezes')

print('exemplo 2 - dois em dois\n')
for i in range(0, 10, 2):
    print(i, 'número')

print('exemplo 3 - decrescente\n') #repetição decrescente
for i in range(10, 0, -1):
    print(i, 'número')

print('\nrepetição com listas 4.1\n')

alunos = ['matheus', 'adriano', 'otávio', 'kayky']
for a in alunos:
    print(a)

print('\nrepetição com listas 4.2 - Imprime posição e nome\n')
alunos = ['matheus', 'adriano', 'otávio', 'kayky']
for index, nome in enumerate(alunos):
    print(index, nome)