#Argumentos Default e Non-default

def boas_vindas(x, y):
    print(f'Ola {x}')
    print(f'Temos {y} leptops em estoque')

print('--------------------------------------')
boas_vindas('Paulo')# vai dar erro
print('--------------------------------------')
boas_vindas('Marcos', 4, 4)# vai dar erro
print('--------------------------------------')
boas_vindas('Linda', 5)# certo
print('--------------------------------------')