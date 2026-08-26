lista_de_compras = []

while True:
    print("\n--- LISTA DE COMPRAS ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Visualizar lista")
    print("4. Sair")
    
    opcao = input("Escolha uma opção (1-4): ")

    if opcao == "1":
        item = input("Digite o nome do item a adicionar: ").strip()
        if item:
            lista_de_compras.append(item)
            print(f"'{item}' foi adicionado à lista.")
    elif opcao == "2":
        item = input("Digite o nome do item a remover: ").strip()
        if item in lista_de_compras:
            lista_de_compras.remove(item)
            print(f"'{item}' foi removido da lista.")
        else:
            print(f"'{item}' não foi encontrado na lista.")
    elif opcao == "3":
        print("\n=== Sua Lista de Compras ===")
        if not lista_de_compras:
            print("A lista está vazia.")
        else:
            for i, item in enumerate(lista_de_compras, 1):
                print(f"{i}. {item}")
    elif opcao == "4":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")

aluno = {
    "nome": "Maria Silva",
    "idade": 17,
    "notas": [8.5, 9.0, 7.5]
}

print("=== Dados do Aluno ===")
print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']} anos")
print(f"Notas: {', '.join(map(str, aluno['notas']))}")

media = sum(aluno["notas"]) / len(aluno["notas"])
print(f"Média: {media:.2f}")

numeros = [12, 7, 5, 18, 22, 9, 3, 14, 30, 11]

pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"Números originais: {numeros}")
print(f"Números Pares: {pares}")
print(f"Números Ímpares: {impares}")

#desafio extra-agenda de contatos

agenda = {}

while True:
    print("\n--- AGENDA DE CONTATOS ---")
    print("1. Adicionar contato")
    print("2. Remover contato")
    print("3. Buscar contato")
    print("4. Sair")
    
    opcao = input("Escolha uma opção (1-4): ")

    if opcao == "1":
        nome = input("Digite o nome do contato: ").strip()
        telefone = input("Digite o telefone: ").strip()
        agenda[nome] = telefone
        print(f"Contato '{nome}' salvo com sucesso!")
        
    elif opcao == "2":
        nome = input("Digite o nome do contato a remover: ").strip()
        if nome in agenda:
            del agenda[nome]
            print(f"Contato '{nome}' removido.")
        else:
            print("Contato não encontrado.")
            
    elif opcao == "3":
        nome = input("Digite o nome do contato a buscar: ").strip()
        if nome in agenda:
            print(f"📱 {nome}: {agenda[nome]}")
        else:
            print("Contato não encontrado.")
            
    elif opcao == "4":
        print("Encerrando a agenda...")
        break
    else:
        print("Opção inválida! Tente novamente.")