# ATIVIDADE_2

import os
os.system("cls")

# Solicitando dois números do usuário

num1= float(input("Digite o primeiro número: "))
num2= float(input("Digite o segundo número: "))

# Calculo dos resultados

media = (num1 + num2) / 2
soma = num1 + num2
produto = num1 * num2
menor = min(num1 , num2)
maior = max(num1 , num2)

# Exibe os resultados

print(f"Média:", {media})
print(f"Soma:", {soma})
print(f"Produto:", {produto})
print(f"Menor valor:", {menor})
print(f"Maior valor:", {maior})

# Verificação de igualdade

if num1 == num2:
    print("{Os números são iguais}")
else:
    print("{Os números são diferentes}")