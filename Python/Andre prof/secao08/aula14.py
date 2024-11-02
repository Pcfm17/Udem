#Sets com strings
'''
similar a listas
evita itens duplicados
nao utiliza index
'''

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.union(set2) #uniao entre as duas sets, ignorando os repitidos
set5 = set1.difference(set3) # mostra a diferenca entre o set1 para o set3
set6 = set1.intersection(set2) #mostra apenas o que tem nas dois sets, mostrando apenas o (a)
set7 = set1.symmetric_difference(set3) #mostra todas as letra menos as repetidas, ou seja retira todos os duplicados

print('--------------------------')
print(set4)
print('--------------------------')
print(set5)
print('--------------------------')
print(set6)
print('--------------------------')
print(set7)