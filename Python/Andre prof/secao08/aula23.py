#Entendendo List Comprehension com Strings
'''
1) mais simples de se escrever
2) utillizar quando voce precisa criar uma nova lista a partir de uma existente
3) [expressao for item in items]
'''

'''frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']

frutas2 = [iten for iten in frutas1 if 'k' in iten]
print(frutas2)
print('------------------------')
#eu
print(list(iten for iten in frutas1 if 'b' in iten))
print('------------------------')'''
#pratica
lista1 = ['abacaxi', 'mamao', 'pera', 'maca']
print(list(iten for iten in lista1 if 'b' in iten))
print('----------------------------------')
fruta = ['agua', 'cerveja', 'coca', 'coco', 'refri']
print(list(iten for iten in fruta if 'c' in iten))
print('----------------------------------')
#ou
print('-------------------------------')
compra = ['cachaça', 'coco', 'bebida']
lista2 = []
for itens in compra:
    if 'b' in itens:
        lista2.append(itens)

print(lista2)
print('----------------------------------')
lista3 = ['vermelho', 'preto', 'azul', 'roxo']
lista4 = []
for itens in lista3:
    if 'v' in itens:
        lista4.append(itens)

print(lista4)

#ou
'''frutas2 = []

for itens in frutas1:
    if 'b' in itens:
        frutas2.append(itens)

print(frutas2)'''