#Visualizando Itens, Keys e Values

#prof
aluno = {'Nome: ': 'Ana', 
        'Idade: ': 16,
        'nota_final: ': 'A',
        'Aprovacao: ': True,
        'Matérias: ': ['Física', 'Matemática', 'Inglês']
        }

print('----------------------')
print(aluno.values())
print('----------------------')
print(aluno.items())
print('----------------------')
print(aluno.keys())
print('----------------------')
print(aluno)
print('----------------------')
print(len(aluno))
print('----------------------')
print(aluno.get('Matérias: '))
