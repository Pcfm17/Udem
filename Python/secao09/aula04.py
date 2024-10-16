#Adicionando o Else e Finally

try:
    valor = int(input('Digite o valor de seu produto: '))
    print(valor)
except ValueError:
    print('Erro: O valor digitado não é um número inteiro')
#else:
#    print('O usuario digitou o número correto')
#    resultado = valor*2
#    print(f'O valor do produto é {resultado}')

finally:
    print('Fim do programa')


print('mais codigo abaixo.')