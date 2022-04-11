print("Limite da pista 80km/h")
vel = float(input("Qual a velocidade: "))

n = (vel - 80) * 7

if vel > 80:
    print("você foi multado!!!")
    print(f"A multa vai custar R${n}")
else:
    print ("Você está dentro do limite da pista!")