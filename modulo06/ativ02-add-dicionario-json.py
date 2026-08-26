import json

clientes = {
    1: {"nome": "Ana Silva", "email": "ana@email.com"},
    2: {"nome": "Carlos Souza", "email": "carlos@email.com"}
}


with open("clientes.json", "w", encoding="utf-8") as arquivo:
    json.dump(clientes, arquivo, indent=4, ensure_ascii=False)


with open("clientes.json", "r", encoding="utf-8") as arquivo:
    dados_carregados = json.load(arquivo)
    print("Dados dos clientes carregados do JSON:")
    print(dados_carregados)