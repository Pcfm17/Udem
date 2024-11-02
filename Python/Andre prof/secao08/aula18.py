#Conhecendo a Função Lambda
'''
1) é uma fincão (pequena) sem nome
2) pode ter vários argumentos mas somente 1 expressão
3) muito utilizada dentro de outras funções
4) codigo mais 'clean

def somar(x):
    return x + 10

print(somar(2))
'''
#argumento:   expressão
somar10 = lambda x, y: x + y + 10

print(somar10(2, 5))