import os
os.system("cls")

idade = int(input("Digite sua idade: "))

if idade >= 18 and idade <= 65:
    print("A pessoa é obrigada a votar!")
else:
    print("A pessoa não é obrigada a votar!")