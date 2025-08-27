import os
os.system("cls")

# Quantidade

qtd = int(input("Digite a quantidade de maçãs desejadas: "))

# PREÇO

if qtd < 12:
    preco = 1.30
else:
    preco = 1.00

# VALOR TOTAL

total = qtd * preco

# RESULTADO

print(f"Quantidade de maçãas: {qtd}")
print(f"Preço por maçã: {preco: .2f}")
print(f"Valor total da compra: R${total: .2f}")