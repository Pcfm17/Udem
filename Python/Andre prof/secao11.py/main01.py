from funcoes01 import somar,multi, find_index
from items.cadrastro import cliente

lista1 = ["a", "b", "c", "d", "e"]

while True:
    print('----------------------------------------------------')
    deseja = input("Deseja (somar ou multiplicar):\nescreva somar para somar e multi para multiplicar: ")
    print('----------------------------------------------------')
    if deseja == "somar":
        somar()
    else:
        multi()
    quer = input('Quer encerrar o programa?: ')
    if quer == 'sim':
        break

    print('----------------------------------------------------')
    cliente()
    print('----------------------------------------------------')
    var1 = find_index(lista1, 'b')
    print(var1)
    print('----------------------------------------------------')