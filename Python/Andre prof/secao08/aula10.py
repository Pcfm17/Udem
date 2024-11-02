#Entendendo sobre Tuples
valores = [1, 2, 3, 4]
cores_lista = ["Amarelo", "Preto", "Azul", "Laranja"]
cores_tuple = ("Amarelo", "Preto", "Azul", "Laranja")

print(cores_lista)
print(cores_tuple)

cores_lista.append("Roxo")

print(cores_lista)
for i in valores:
    print("------------------------------------")
    print(f"Cor: {cores_lista[valores.index(i)]} - Valor- {i}")
    print("------------------------------------")