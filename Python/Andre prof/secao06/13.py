#Criando condições com while loop
'''
1) excelente para loops dependetes de uma codicao
2) publicar um produto com comissao de 10% se for acima de R$20
'''

valor = float(input('Custo do produto: '))

while valor > 20:
    comissao = valor * 0.1 + valor
    print(f'O valor final do seu produto será de R$ {comissao:.2f}')
    break