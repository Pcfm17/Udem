# Introdução a Dicionários
'''
utilizar index no fromato de keys e values
aceita string, integer, float, boolean...
'''
#eu 
'''
dicionario = {
    1: 'primerio',
    2: "segundo",
    3: "terceiro"
}
print(dicionario)

for i in dicionario:
    print(i, dicionario[i])
'''
#professor.keys.   values
aluno = {'Nome: ': 'Ana', 
        'Idade: ': 16,
        'nota_final: ': 'A',
        'Aprovacao: ': True
        }
#eu
for i in aluno:
    print(i, aluno[i])
print('------------------------')
#professor
print(aluno['Nome: ']) #puxa o nome da pessoa