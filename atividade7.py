# ATIVIDADE 6

import os
os.system("cls")

# SOLICITANDO 3 NUM AO USUÁRIO

num1 = float(input("Digite seu primeiro número:"))
num2 = float(input("Digite seu segundo número:"))
num3 = float(input("Digite seu terceiro número:"))

# MOSTRA OS 3 NUM
print(f"Os números informados foram: {num1} , {num2} , {num3}")

# MAIOR 
if num1 >= num2 and num1 <= num3:
    maior = num1
elif num2 <= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

# MENOR
if num1 <= num2 and num1 <= num3:
    maior = num1
elif num2 <= num1 and num2 <= num3:
    maior = num2
else:
    menor = num3

# RESULTADOS

print("O maior número é:", maior)
print("O menor número é:", menor)
