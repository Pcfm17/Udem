while True:
    print('__________IMFORMAÇÕES__________')
    altura  = float(input('Qual é a sua altura em cm: '))
    peso = float(input('Qual é o seu peso em Kg: '))
    print('_______________________________')
    imc = peso / (altura/100)**2
    if imc < 18.5:
        print('MAGREZA')
    elif 18.5 <= imc <= 24.9:
        print('NORMAL')
    elif 25 < imc <= 29.9:
        print('SOBREPESO')
    elif 30 < imc <= 39.9:
        print('OBESIDADE')
    elif imc > 40:
        print('OBESIDADE GRAVE')
    else:
        print('ERRO')