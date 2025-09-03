import os
os.system("cls")

print("=== CARDÁPIO DO RESTAURANTE ===")
print("""
Código \t\t Prato \t\t\t Valor
      
prinr() # linha em branco
      
         1 \t Picanha \t\t- {R$ 25,00}
         2 \t Lasanha \t\t- {R$ 20,00}
         3 \t Strogonoff \t\t- {R$ 18,00}
         4 \t Bife Acebolado \t- {R$ 15,00}
         5 \t Pão com ovo \t\t- {R$ 5,00}
      """)

print() # linha em branco

codigo = int(input("Digite o código do prato desejado: "))

print()  # linha em branco

match codigo:
    case 1:
        print("{Você escolheu: Picanha - R$ 25,00}")
    case 2:
        print("{Você escolheu: Lasanha - R$ 20,00}")
    case 3:
        print("{Você escolheu: Strogonoff - R$ 18,00}")
    case 4:
        print("{Você escolheu: Bife Acebolado - R$ 15,00}")
    case 5:
        print("{Você escolheu: Pão com ovo - R$ 5,00}")
    case _:
        print("{Código inválido! Tente novamente.}")

print()  # linha em branco