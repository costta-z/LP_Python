import os
os.system("cls")

#ENTRADA DE DADOS

num1 = float(input("Digite seu primeiro número:"))
num2 = float(input("Digite seu segundo número:"))
operador = input("Digite seu operador (+, -, *, /): ")

# ESTRUTURA
match operador:
    case "+":
        resultado = num1 + num2
    case "-":
        resultado = num1 - num2
    case "*":
        resultado = num1 * num2
    case "/":
        if num2 !=0:
            resultado = num1 / num2
        else:
            resultado = "ERRO! Divisão por zero."
    case _:
        resultado = "Operador inválido!"

# SAIDA

print(f"Números informados: {num1} e {num2}")
print(f"Operador informado:")
print(f"Resultado: {resultado}")
    