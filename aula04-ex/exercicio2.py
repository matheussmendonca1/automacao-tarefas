'''
Exercício 2

Crie um programa que recebe dois números reais como entrada e um operador matemático. De acordo com o operador matemático fornecido, o programa deve calcular e apresentar o resultado da operação.
'''

print('Insira o primeiro valor: ') 
num1 = int(input())

print('Insira o operador matemático (+ - * / ): ') 
operador = input()

print('Insira o segundo valor: ')
num2 = int(input())

print(f'Resultado: {eval(str(num1) + operador + str(num2))}\n')