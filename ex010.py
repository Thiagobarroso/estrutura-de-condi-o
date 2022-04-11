print ('=-'*20)
print ("Aumento de salário, eba!")
print ('=-'*20)

sal = float(input("Digite seu salário: "))

au10 = sal + (sal * (10/100))
au15 = sal + (sal * (15/100))

if sal > 1250:
    print(f"Seu salário aumentou para: R${au10}")
else:
    print(f"O seu salário aumentou para: R${au15}")