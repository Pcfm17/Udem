#Concatenando listas

numeros = [1, 2, 3, 4, 5]
letras = ["a", "b", "c", "d"]

#final = numeros * 2 esse faz com que apareca repetidamente os valores descritos no numeros
#final = numeros + letras
#ou
numeros.extend(letras)

print(numeros)