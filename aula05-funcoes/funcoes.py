'''
def nome_funcao(param1, param2):
    faz algo
    retorna um valor
'''

#func 1
def calcularAreaTriangulo(base, altura):
    area = (base * altura) / 2
    return print(f'{area}')


#func 2
def login(usuario, senha):
    if usuario == 'admin' and senha == '1234':
        return print(f'Olá, {usuario}')
    else:
        return False
    
#calcularAreaTriangulo(3, 5)
#login('admin', 1234)