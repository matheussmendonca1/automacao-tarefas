#Estrutura de repetição for

for times in range(1, 5):  #O comando "range" cria um intervalo de valores, no caso do "times", ele vai criar um loop que vai ser executado 5 vezes

    nome = input('Digite o nome do aluno: \n')
    nota = int(input('Digite a nota do aluno: \n'))

    if nota >= 6:
        print(f"{nome} foi aprovado")
    else:
        print(f"{nome} foi reprovado com a nota {nota: .2f}")
