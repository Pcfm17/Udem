# Funções em sets

lista1 = set([1, 2, 3, 4, 5, 6]) #lista, class= set
s1 = {1, 2, 3, 4, 5, 6} #set, class=set
s1.add(7) # para adicionar numeros
s2 = {1, 2, 3, 4, 5, 6, 2, 3, 6} 
s3 = {1, 2, 3, 4, 5, 6, 2, 3, 6} 
s3.add(4)
s4 = {1, 2, 3, 4, 5, 6, 2, 3, 6}
s4.update([7, 8, 9, 10]) #faz acrescentar numeros, se colocar numeros repetidos ele vai iguinorar
# Qual a diferenca entre remove e discard?
# remove: se o elemento não estiver no set ele vai dar um erro
# discart: se o elemento não estiver no set ele vai continuar o codigo sem nenhum erro
s1.remove(1) #faz remover o numero
s1.discard(4) #faz dercatar o numero

print("-----------------------------")
print(s1)
print("-----------------------------")
print(s4)
print("-----------------------------")
print(s3) #se adicionar numeros que ja tem em uma lista, nao vai aparecer ele duas vezes ou mais so vai aparecer apenas uma vez
print("-----------------------------")
print(s2) #mostra todos osumeros apenas um vez em vez de mostrar numeros repetidos tambem
print("-----------------------------")
print(s1)
print("-----------------------------")
print(lista1)
print(s1)
print("-----------------------------")
#para aparecer a class
print(type(lista1))
print(type(s1))
print("-----------------------------")