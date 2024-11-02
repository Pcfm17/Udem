#Verificando itens em uma lista

cores = ["Amarelo", "Verde", "Azul", "Vermelho"]

while True:
    deseja_cor = input("Quer qual cor para su compra: ")
    if deseja_cor == "amarelo":
        print("O item está na lista")
        print("Tem certeza que deseja esta cor. Custo: R$ 500")
    elif deseja_cor == "verde":
        print("O item está na lista")
        print("Tem certeza que deseja esta cor. Custo: R$ 570")
    elif deseja_cor == "azul":
        print("Esta cor ão está na lista")
    elif deseja_cor == "vermelho":
        print("O item está na lista")
    else:
        print("O item não está na lista")
        cor = input("Qual cor vc deseja adicionar nesta lista: ")
        cores.append(cor)
        print(cores)