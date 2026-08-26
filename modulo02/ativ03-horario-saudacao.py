from datetime import datetime

agora = datetime.now()
hora_formatada = agora.strftime("%H:%M:%S")

nome = input("Digite o seu nome: ")

print(f"Olá, {nome}! Agora são {hora_formatada}. Seja bem-vindo(a)!")