import os
os.system("cls")

dia = int(input("Digite um número para o dia da semana: "))

print() # linha em branco

match dia:
    case 1:
        print("Domingo - {Final de semana}")
    case 2:
        print("Segunda-feira - {Dia útil}")
    case 3:
        print("Terça-feira - {Dia útil}")
    case 4:
        print("Quarta-feira - {Dia útil}")
    case 5:
        print("Quinta-feira - {Dia útil}")
    case 6:
        print("Sexta-feira - {Dia útil}")
    case 7:
        print("Sabado - {Final de semana}")
    case _:
        print("{Dia inválido.}")