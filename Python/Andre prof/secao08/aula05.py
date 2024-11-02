#Extraindo variáveis de Listas

produto = ["Arroz", "Feijão", "Laranja", "Banana", 1, 5, 8]

item1, item2, item3, *outros, item6 = produto

print(item1, item2, item3, outros)
print("------------------------------------------")
print(outros)

print(item1)
print(item2)
print(item3)
print(item6)
