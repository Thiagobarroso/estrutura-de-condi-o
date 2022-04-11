print("Cálculo, para as férias:")
dist = float(input("Qual a distância da viagem em Km? "))

n1 = dist * 0.50
n2 = dist * 0.45

if dist <= 200:
    print(f"Você pagará total R${n1}")
else:
    print(f"Você pagagará R${n2}")