import os
os.system("cls")

import math

# Entrada de dados
sexo = input("Digite o sexo (M para masculino, F para feminino): ").strip().upper()
altura = float(input("Digite a altura em metros: "))

# Usando match-case
match sexo:
    case "M":
        peso_ideal = (72.7 * altura) - 58
        print(f"Peso ideal (masculino): {peso_ideal:.2f} kg")
    case "F":
        peso_ideal = (62.1 * altura) - 44.7
        print(f"Peso ideal (feminino): {peso_ideal:.2f} kg")
    case _:
        print("Sexo inválido! Digite apenas M ou F.")