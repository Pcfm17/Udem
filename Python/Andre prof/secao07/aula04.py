#Parâmetros e Argumentos em uma função
'''
def bem_vindo_Marcos():
    print('Ola Marcos')
    print('Temos 5 leptops em estoque')

def bem_vindo_Ronaldo():
    print('Ola Ronaldo')
    print('Temos 5 leptops em estoque')

def bem_vindo_linda():
    print('Ola linda')
    print('Temos 5 leptops em estoque')

print('--------------------------------------')
bem_vindo_Marcos()
print('--------------------------------------')
bem_vindo_Ronaldo()
print('--------------------------------------')
bem_vindo_linda()
print('--------------------------------------')
'''

def boas_vindas(x, y):
    print(f'Ola {x}')
    print(f'Temos {y} leptops em estoque')

print('--------------------------------------')
boas_vindas('Paulo', 6)
print('--------------------------------------')
boas_vindas('Marcos', 4)
print('--------------------------------------')
boas_vindas('Linda', 5)
print('--------------------------------------')