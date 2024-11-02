while True:
    print('_______________INFORMAÇÕES_______________')
    print('Em "F" vai de 120 até 169.\nEm "C" vai de 48 até 77.')
    print('==================PEDIDO==================')
    try:
        eat = float(input('Qual é a temperatura da carne: '))
    except ValueError:
        print('==========ERRO=========')
        print('Só aceitamos números')
        print('==========ERRO=========')
    print('_________________________________________')
    print('Temperatura - Cozimento')
    if 130 > eat >= 120 or 54 > eat >= 48:
        print(f'{eat}F ou 48C - Rare (Selada)')
    elif 140 > eat >= 130 or 60 > eat >= 54:
        print(f'{eat}F ou 54C - Medium rare (Ao ponto para o mal)')
    elif 150 > eat >= 140 or 65 > eat >= 60:
        print(f'{eat}F ou 60C - Medium (Ao ponto)')
    elif 160 > eat >= 150 or 71 > eat >= 65:
        print(f'{eat}F ou 65C - Medium well (Ao ponto para o bem)')
    elif 170 > eat >= 160 or 78 > eat >= 71:
        print(f'{eat}F ou 71C - Well done (Bem passado)')
    else:
        print('NÃO É POSSÍVEL, POIS VAI SER QUEIMADO.')
    print('-----------------------------------------')
    print('SEU PEDIDO FOI FEITO COM SUCESSO')
    print('-----------------------------------------')