#Função Map em uma lista
'''
1) muito utilizado som listas
2) aplicar uma função a um Iterable, por items. (list, tuplas, dicionário)
'''

lista1 = [1, 2, 3, 4]

def multi(x):
    return x * 2

print(multi(2))
print('---------------------------')
lista2 = map(multi, lista1)
print(list(lista2))