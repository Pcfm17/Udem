usuario = input("Qual é o seu nome?: ")
idade = int(input("Qual é a sua idade?: "))



def compra():
    if idade >= 18 and idade <= 120:
        n1 = input("Voce vai querer eletronico, alimento ou livro: ")
        if n1 == "eletronico":
            n2 = input("Qual dos tres eletronicos vc deseja (PS4, Computador ou celular): ")
            if n2 == "PS4":
                print("custa R$3500")
                n3 = input("O senhor deseja continur com a compra?: ")
                if n3 == "sim":
                    cartao = int(input("Digite a senha do cartão:"))
                    n4 = int(input("Digite novamente para a confirmação: "))
                    if cartao == n4:
                        print("A sua encomenda esta sendo preparada.")
                        return("Irá chegar em 2 semanas")
                    else:
                        return("A senha nãp está certa.")
                else:
                    return("A compra está sendo canselada.")


            elif n2 == "computador":
                print("custa R$4500")
                n3 = input("O senhor deseja continur com a compra?: ")
                if n3 == "sim":
                    cartao = int(input("Digite a senha do cartão:"))
                    n4 = int(input("Digite novamente para a confirmação: "))
                    if cartao == n4:
                        print("A sua encomenda esta sendo preparada.")
                        return("Irá chegar em 1 semanas")
                    else:
                        return("A senha nãp está certa.")
                else:
                    return("A compra está sendo canselada.")


            else:
                print("custa R$2500")
                n3 = input("O senhor deseja continur com a compra?: ")
                if n3 == "sim":
                    cartao = int(input("Digite a senha do cartão:"))
                    n4 = int(input("Digite novamente para a confirmação: "))
                    if cartao == n4:
                        print("A sua encomenda esta sendo preparada.")
                        return("Irá chegar em 4 dias.")
                    else:
                        return("A senha nãp está certa.")
                else:
                    return("A compra está sendo canselada.")


        elif n1 == "alimento":
            n5 = input("Qual dos desses o senhor vai querer? (salada, fruta ou massa): ")
            if n5 == "salada":
                n6 = input("Vai querer muito ou pouca salada?: ")
                if n6 == "pouca":
                    print("OK, senhor já está sendo preparado.")
                    return("Chegará em 25 a 35 minutos.")
                if n6 == "muito":
                    print("OK, senhor já está sendo preparado.")
                    return("Chegará em 35 a 45 minutos.")


            elif n5 == "fruta":
                n7 = input("Qual dessas frutas voce vai querer. (melao, banana ou maça)")
                if n7 == "melao":
                    print("O melão custa R$: 8")
                    n8 = input("O senhor deseja continuar com a compra?: ")
                    if n8 == "sim":
                        cartao = int(input("Digite a senha o cartão: "))
                        n9 = int(input("Digite novamente para a confirmação: "))
                        if cartao == n9:
                            return("A sua encomenda está a caminho.")
                        else:
                            return("A senha não está certa.")
                    else:
                        return("A compra está sendo cancelada.")


                elif n7 == "banana":
                    print("O banana custa R$: 10 a unidade")
                    n8 = input("O senhor deseja continuar com a compra?: ")
                    if n8 == "sim":
                        cartao = int(input("Digite a senha o cartão: "))
                        n9 = int(input("Digite novamente para a confirmação: "))
                        if cartao == n9:
                            return("A sua encomenda está a caminho.")
                        else:
                            return("A senha não está certa.")
                    else:
                        return("A compra está sendo cancelada.")


                else:
                    print("O maça custa R$: 5")
                    n8 = input("O senhor deseja continuar com a compra?: ")
                    if n8 == "sim":
                        cartao = int(input("Digite a senha do cartão: "))
                        n9 = int(input("Digite novamente para a confirmação: "))
                        if cartao == n9:
                            return("A sua encomenda está a caminho.")
                        else:
                            return("A senha não está certa.")
                    else:
                        return("A compra está sendo cancelada.")


            else:
                n10 = input("O senhor vai querer a massa fina ou grossa: ")
                if n10 == "fina":
                    print("A massa fina custa R$: 30.")
                    n11 = input("O senhor deseja continuar com a compra?: ")
                    if n11 == "sim":
                        cartao = int(input("Digite a senha do cartão: "))
                        n12 = int(input("Digite novamente para a confirmação: "))
                        if cartao == n12:
                            print("A sua encomenda está a caminho.")
                            return("Chegará em 45 a 55 minutos.")
                        else:
                            return("A senha não está certa.")
                    else:
                        return("A compra está sendo cancelada.")


                else:
                    print("A massa fina custa R$: 35.")
                    n11 = input("O senhor deseja continuar com a compra?: ")
                    if n11 == "sim":
                        cartao = int(input("Digite a senha do cartão: "))
                        n12 = int(input("Digite novamente para a confirmação: "))
                        if cartao == n12:
                            print("A sua encomenda está a caminho.")
                            return("Chegará em 55 minutos a 1h.")
                        else:
                            return("A senha não está certa.")
                    else:
                        return("A compra está sendo cancelada.")


        else:
            n13 = input("Qual dos dois voce vai querer. (a arte da guerra ou senhor dos aneis): ")
            if n13 == "a arte da guerra":
                print("O a arte da guerra custa R$: 50.")
                n14 = input("O senhor deseja continuar com a compra?: ")
                if n14 == "sim":
                    cartao = int(input("Digite a senha do cartão: "))
                    n15 = int(input("Digite novamente a senha: "))
                    if cartao == n15:
                        print("A sua encomenda está a caminho.")
                        return("Cegará em uma semanas.")
                    else:
                        return("A senha não está certa.")
                else:
                    return("A compra está sendo cancelada.")
            

            else:
                print("O senhor dos aneis custa R$: 40.")
                n14 = input("O senhor deseja continuar com a compra?: ")
                if n14 == "sim":
                    cartao = int(input("Digite a senha do cartão: "))
                    n15 = int(input("Digite novamente a senha: "))
                    if cartao == n15:
                        print("A sua encomenda está a caminho.")
                        return("Cegará em uma semanas.")
                    else:
                        return("A senha não está certa.")
                else:
                    return("A compra está sendo cancelada.")
    

    else:
        return("A sua compra está sendo cancelada pois voce não tem idade o suficiente.")


print(compra())