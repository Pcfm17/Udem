# Looping dentro de um dicionário

#eu
while True:
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    nota_final = input('Nota_final: ')
    print('------------------------------')
    def aprovado():
        if nota_final.upper() == 'A' or nota_final.upper() == 'B' or nota_final.upper() == 'C':
            return('Aprovado')
        else:
            return('Reprovado')

    aluno = {'Nome: ': nome, 
            'Idade: ': idade,
            'nota_final: ': nota_final,
            'Aprovacao: ': aprovado()
            }
    print('------------------------------')
    for i in aluno:
        print(i, aluno[i])
    print('------------------------------')
        


print('--------------------------')
#prof
for keys, values in aluno.items():
    print(keys, values)

'''#eu
for x in aluno:
    print(x, aluno[x])  # imprime o valor de cada chave e o valor associ
'''