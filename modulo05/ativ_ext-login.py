usuarios_cadastrados = {
    "admin": "1234",
    "joao": "senha123",
    "maria": "python2026"
}

def validar_login(usuario, senha):
    if usuario in usuarios_cadastrados and usuarios_cadastrados[usuario] == senha:
        return True
    return False

user = input("Digite o usuário: ")
passw = input("Digite a senha: ")

if validar_login(user, passw):
    print("Login realizado com sucesso!")
else:
    print("Usuário ou senha incorretos.")