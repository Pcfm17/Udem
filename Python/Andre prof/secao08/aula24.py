#Entendendo List Comprehension com números
'''
1) mais simples de se excrever
2) utillizar quando voce precisa criar uma nova lista a partir de uma existente
3) [expressao for item in items]
'''

'''valores = []
for x in range(6):
    valores.append(x * 10)

print(valores)

#ou

valores = [x * 10 for x in range(6)]
print(valores)'''

#pratica
numero = []
for x in range(6):
    numero.append(x * 10)

print(numero)

print('-----------------------------------')
#ou
numero1 = [x * 10 for x in range(6)]
print(numero1)