def somar():
    print('Esta função vai somar valores.')
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite outro numero: "))
    soma = num1 + num2
    print('----------------------------------------------------')
    print(f"A soma dos dois números é: {soma}")
    print('----------------------------------------------------')


def multi():
    print('Esta função vai muitiplicar valores.')
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite outro numero: "))
    multiplicar = num1 * num2
    print('----------------------------------------------------')
    print(f"A multiplicação dos dois números é: {multiplicar}")
    print('----------------------------------------------------')

def find_index(to_find, item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return i
    return -1