#Função Filter
'''
1) muito utilizado com listas
2) aplicar uma função a um Iterable, filtrando items. (list, tuple, dicionario, etc.)
'''

valores = [10, 12, 32, 44, 57]

def remover20(x):
    return x > 20

print(list(map(remover20, valores)))
print('------------ou-------------')
print(list(filter(remover20, valores)))
print('------------ou-------------')
print(list(filter(lambda x: x > 20, valores)))


#eu
#print(list(filter(lambda x: x > 20, valores)))