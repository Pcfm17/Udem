#Agregando Duas listas com o Zip

cores = ["Amarelo", "Preto", "Azul", "Laranja"]
valores = [10, 20, 30, 40]

duas_listas = zip(cores, valores)

print(list(duas_listas))
for x in valores:
    print(f"{cores[valores.index(x)]} - {x}")