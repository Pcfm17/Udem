#for loop- criando um retangulo
'''
Tem que fazer assim
criar um retangulo 6x6:
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
'''
linhas = 6
colunas = 6
simbulo = '@'

for l in range(linhas):
    for c in range(colunas):
        print(simbulo, end='')
    print()