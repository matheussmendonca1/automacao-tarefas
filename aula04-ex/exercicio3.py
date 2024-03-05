'''
Exercício 3

Crie um programa que execute repetidamente o programa do exercício 2. Após a apresentação do resultado, o programa deve perguntar se o usuário deseja continuar a calcular, se a resposta  for S (sim), o programa deve continuar; se a resposta dor N (não), o programa deve terminar.
'''

res = True
while res == True:

    print('Insira o primeiro valor: ') 
    num1 = int(input())

    print('Insira o operador matemático (+ - * / ): ') 
    operador = input()

    print('Insira o segundo valor: ')
    num2 = int(input())

    print(f'Resultado: {eval(str(num1) + operador + str(num2))}\n')

    print('Pretende continuar?' )
    resposta = str(input())

    if resposta == 's': 
        res = True
    
    elif resposta == 'n':
        break


