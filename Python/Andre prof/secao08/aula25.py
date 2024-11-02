#Lista e Generator Expressions
'''
1) uma forma mais para listas, dicionario e etc;
2) menos memória alocada
3) valores em bytes
'''
from sys import getsizeof

numeros = [x * 10 for x in range(100)]
print(type(numeros))
print(list(numeros))
print(getsizeof(numeros))

print('----------------------------------------')

numeros1 = (x * 10 for x in range(100))
print(type(numeros1))
print(list(numeros1))
print(getsizeof(numeros1))