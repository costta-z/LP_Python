# ATIVIDADE 5

import os
os.system("cls")

idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Você não pode votar. ")
elif (idade >= 16 and idade <18) or (idade > 65):
    print("Seu voto é opcional.")
else:
    print("Seu voto é obrigatório")