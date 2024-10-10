nome = input("Qual é o seu nome: ")
cpf = int(input("Digite o seu CPF: "))
idade = int(input("Digite a sua idade: "))
servico = input("Qual voce deseja comprar ou vender?: ")


def venda():
    if idade >= 18:
        n = input(f"O seu nome: {nome}, CPF: {cpf}. Está correto?: ")
        n3 = input("Voce tem alguma experiencia na profissão de vendedor: ")
        if n == "sim" and n3 == "sim":
            return("Iremos entrar em contados em 7 dias uteis.")
        elif n == "sim":
            return("Iremos analizar o seu curriculo.")
        else:
            return("Voce infelizmente não foi aprovado.")
    else:
        return("Sinto muito, mas infelizmente não iremos comtratar voce: ")





def compra():
    if idade >= 18:
        n1 = input(f"O seu nome: {nome}, CPF: {cpf}. Está correto?: ")
        cartao = int(input("Digite a sua senha de cartão: "))
        n2 = int(input("Comfirmação da senha do cartão, digite novamente: "))
        if n1 == "sim" and n2 == cartao:
            print("OK, A sua encomenda já esta sendo enbalada.")
            return("Irá chegar de 10 a 15 dias.")
        elif n1 == "nao":
            return("A compra foi canselada.")
        else:
            return("Sua senha está incorreta.")
    else:
        print("Voce não esta permitido a fazer a compra.")
        return("A compra será permetida a partir de 18 anos.")


if servico == "vender":
    print(venda())
elif servico == "compra":
    print(compra())
else:
    print("Erro")