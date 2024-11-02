#Criando Sets
'''
similar a listas
envia itens duplicados
nao utilizar index
'''

lista1 = [10, 20, 30, 40, 50]
lista2 = [10, 20, 60, 70]

num1 = set(lista1)
num2 = set(lista2)

print(num1 | num2) # (uniao)esta misturando as duas listas tirando o repetidos , porem está fora de ordem
print( num1 - num2) #diference
print(num1 ^ num2) #(symetric diference) faz aparecer apenar os numeros que nao sao repitidos
print(num1 & num2) #(and)mostra apenas os numeros repetidos
#print(num1 num2)
print(len(num1)) #mostra a quantidade de numeros na lista 1, que no caso tem apeas 5
print(num1.intersection(num2)) #mostra os numeros repetidos
print(num1.union(num2)) #mostra os numeros repetidos e deixa como se tivesse apenas um deles é a uniao, igual o primeiro
print(num1[0]) # vai dar erro pq perdeu os index dele 