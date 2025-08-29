import os
os.system("cls")

# Dados já cadastrados
login_cadastrado = "usuario123"
senha_cadastrado = "senha123"

# Solicitando dados do usuario

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

# Verificando

if login == login_cadastrado and senha ==  senha_cadastrado:
    print("Bem-Vindo!")
else:
    print("Login ou senha inválidos.")