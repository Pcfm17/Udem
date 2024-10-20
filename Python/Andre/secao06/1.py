# if, else

velocidade = float(input("Qual sua velocidaed neste momento?: "))

if velocidade > 110:
    print("Voce esta muito rapido.")
    print("Favor reduzir a sua velocidade")

elif velocidade <= 60:
    print("Favor aumente sua velocidade")
    
else:
    print("Velocidade ok")