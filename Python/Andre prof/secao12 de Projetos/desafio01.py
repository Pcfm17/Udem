print('==================PEDIDO==================')
try:
    rendimento = float(input('Qual é o rendimento da lata: '))
    altura = float(input('Qual é a altura da parede: '))
    largura = float(input('Qual é a largura da parede: '))
except ValueError:
    print('---------------------------------------')
    print('SÓ ACEITAMOS VALORES PARA FAZER OS CALCULO')
    print('---------------------------------------')

    
def latas():
    area = altura * largura
    quantidade_lata = area / rendimento
    print('_________________________________________')
    print(f'Você precisa de {quantidade_lata:.1f} latas de tinta.')
    print('_________________________________________')

latas()