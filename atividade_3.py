# ATIVIDADE_

import os
os.system("cls")

# Solicitando dois números do usuário

nota1= float(input("Digite sua nota1: "))
nota2= float(input("Digite sua nota2: "))
nota3= float(input("Digite sua nota3: "))

# Calculo dos resultados

media = (nota1 + nota2 + nota3) / 3
soma = nota1 + nota2 + nota3

if media >= 7:
   Resultado = "Aprovado."
else:
    Resultado ="Reprovado."

    




# Exibe os resultados

print(f"Média:", {media})
print(f"Soma:", {soma})
print(f"Resultado:", {Resultado})



