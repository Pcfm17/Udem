# for loop- ultilizando if e else

#enviar um e-mail com os detalhes da compras online(maximo 3 tentativas)para compras afirmativas

compra_comfirmada = False
dados_compra = 'Compra  no valor de R$12.50 e entrega comfirmada'


for enviar in range(3):
    if compra_comfirmada:
        print(dados_compra)
        print("Detalhes enviados para o seu e-mail.")
        break
    else:
        print("Falha na compra")
        break