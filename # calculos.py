# calculos

import os
os.system("cls") 

#Leitura dos dois números
num1 = float(input  ("Digite seu primeiro número: "))
num2  = float(input  ("Digite seu segundo número: "))

#Calculos
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

#Exibição dos resultados
print("Dados inicias: ")
print("Número 1:, num1")
print("Número 2:, num2")

print(f"Resultados:")
print(f"Soma:", {soma})
print(f"Subtração:", {subtracao})
print(f"Multiplicação:", {multiplicacao})
print(f"Divisão:", {divisao})



