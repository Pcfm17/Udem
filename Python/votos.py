#programa para votar
from time import sleep

votoslula = []
votosbolsonario = []
votos = []

def votar():
    while True:
        try:
            sair = int(input('Para sair digite (-1). Mas para votar digite (1): '))
            if sair == -1:
                break

            elif sair == 1:
                idade = int(input('Qual sua idade: '))
                if 18 <= idade <= 80:
                    print('Você está permitido para votar.')
                    voto = int(input(' 1)Para lula digite: 13:\n 2)Para bolsonario digite: 22:\n 3)Para sair digite: -1:\n'))

                    if voto == -1:
                        break
                    elif voto == 13:
                        deseja = input('Tem certeza do voto? (sim ou nao): ')
                        if deseja.lower() == 'sim':
                            votoslula.append(voto)
                            votos.append(voto)
                            print('O seu voto foi registrado')
                            sleep(5)
                        else:
                            print('Erro. Voto não registrado.')
                            sleep(5)
                    elif voto == 22:
                        deseja = input('Tem certeza do voto? (sim ou nao): ')
                        if deseja.lower() == 'sim':
                            votosbolsonario.append(voto)
                            votos.append(voto)
                            print('O seu voto foi registrado.')
                            sleep(5)
                        else:
                            print('Erro. Voto não registrado.')
                            sleep(5)
                    else:
                        print('Erro. Não digitou o número certo.')
                        sleep(5)

                elif idade >= 100:
                    print('Erro')


                elif 80 <= idade < 100:
                    print('Você está aposentado. Você não precisa votar.')
                    deseja1 = input('Mas, se quiser votar mesmo assim, digite: (sim), mas se não quiser votar, digite: (nao): ')
                    if deseja1.lower() == 'sim':
                        voto = int(input('1)Para lula digite: 13:\n 2)Para bolsonario digite: 22:\n 3)Para sair digite: -1:\n'))
                        if voto == -1:
                            break
                        elif voto == 13:
                            deseja = input('Tem certeza do voto? (sim ou nao): ')
                            if deseja.lower() == 'sim':
                                votoslula.append(voto)
                                votos.append(voto)
                                print('O seu voto foi registrado')
                                sleep(5)
                            else:
                                print('Erro. Voto não registrado.')
                                sleep(5)
                        elif voto == 22:
                            deseja = input('Tem certeza do voto? (sim ou nao): ')
                            if deseja.lower() == 'sim':
                                votosbolsonario.append(voto)
                                votos.append(voto)
                                print('O seu voto foi registrado.')
                                sleep(5)
                            else:
                                print('Erro. Voto não registrado.')
                                sleep(5)
                        else:
                            print('Erro. Não digitou o número certo.')
                            sleep(5)
                    elif idade < 18:
                        print('Você não está permitido para votar, pois não possui idade suficiente.')
                        sleep(5)
                elif idade < 18:
                    print('Você não está permitido para votar, pois não possui idade suficiente.')
                    sleep(5)
                else:
                    print('Erro')
                    sleep(5)
            else:
                print('Erro')
        except ValueError:
            print('Favor digitar um número.')


votar()
print(f'A quantidade de votos no lula: {len(votoslula)}')
print(f'A quantidade de votos no bolsonário: {len(votosbolsonario)}')
print(f'O total de votos registrado: {len(votos)}')