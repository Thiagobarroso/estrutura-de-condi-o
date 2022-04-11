ano = int(input("Digite o ano: "))

bi = ano % 4

if bi == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("Esse ano é Bisexto!!!")
else:
    print("esse ano não é bisexto")

