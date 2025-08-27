import os
os.system("cls")

# DADOS

nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

# MÉDIA
media = (nota1 + nota2) / 2

# CONCEITO

if media >= 9:
    CONCEITO = "A"
elif media >= 7.5:
    CONCEITO = "B"
elif media >= 6:
    CONCEITO = "C"
elif media >= 4:
    CONCEITO = "D"
else:
    CONCEITO = "E"

# SITUAÇÃO
if CONCEITO in {"A", "B", "C"}:
    situacao = "APROVADO"
else:
    situacao = "REPROVADO"

# SAIDA

print("ALUNO:", nome)
print("SITUAÇÃO:", situacao)
print("CONCEITO:", CONCEITO)
print("MÉDIA:", media)



