#Trabalhando com o Try e Except com o input


try:
    valor = int(input('Digite o valor de seu produto: '))
    print(valor)
except ValueError:
    print('Erro: O valor digitado não é um número inteiro')

print('mais codigo abaixo.')










#brincadeira. esquece esse codigo.
'''def trabalhando_com_try_e_except_com_input():
    try:
        idade = int(input("Digite sua idade: "))
    except IndexError:
        print("Erro: Você não digitou nada!")

trabalhando_com_try_e_except_com_input()'''