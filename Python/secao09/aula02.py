#Trabalhando com o Try e Except com uma lista

try:
    letras = ['a', 'b', 'c']
    print(letras[3])
except IndexError:
    print('Index não existe.')