def cliente():
    while True:
        print('Cadrastro do cliente.')
        nome = input('Nome: ')
        idade = input('Idade: ')
        email = input('E-mail: ')
        print('----------------------------------------------------')
        print(f"Nome: {nome}\n Idade: {idade}\n email: {email}")
        print('----------------------------------------------------')
        correto = input("Essas imformações estão corretas?\n(sim ou nao):")
        if correto == "sim":
            print('----------------------------------------------------')
            print("Cadastro realizado com sucesso!")
            print('----------------------------------------------------')
        else:
            print('----------------------------------------------------')
            print("Cadastro não realizado!")
            print('----------------------------------------------------')
        sair = input("Deseja encerra o cadrastro?: (sim ou nao): ")
        if sair == "sim":
            break