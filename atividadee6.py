# ATIVIDADE 6

import os
os.system("cls")

# SOLICITANDO 2 NUM AOS USUÁRIO

num1 = float(input("Digite seu primeiro número:"))
num2 = float(input("Digite seu segundo número:"))

# MOSTRA OS 2 NUM
print(f"Os números informados foram: {num1} e {num2}")

# MAIOR E MENOR
if num1 > num2:
    print(f"O número maior é:  {num1}")
    print(f"O número menor é: {num2}")
elif num2 > num1:
    print(f"O número maior é: {num2}")
    print(f"O número menor é: {num1}")
else:
    print("Os dois números são iguais")