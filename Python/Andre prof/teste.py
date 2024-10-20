renda = float(input("Qual é sua renda?: "))
if renda > 2000:
    print("Voce foi aprovado.")
elif 1500 <= renda <2000:
    print("Voce esta quase sendo aprovado.")
    print("Para ser aprovado necessita no minimo de 2000 reais.")
elif renda == 2000:
    print("Voce foi aprovado.")
else:
    print("Voce foi reprovado")