num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
diferenca = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2 if num2 != 0 else "Divisão por zero não é permitida"
resto = num1 % num2 if num2 != 0 else "N/A"

print(f"Soma: {soma}")
print(f"Diferença: {diferenca}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Resto da divisão (%): {resto}")

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

if num1 > num2:
    print(f"O maior número é {num1}.")
elif num2 > num1:
    print(f"O maior número é {num2}.")
else:
    print("Os dois números são iguais.")

idade = int(input("Digite a sua idade: "))

if idade < 0:
    print("Idade inválida!")
elif idade <= 12:
    print("Classificação: Criança")
elif idade <= 17:
    print("Classificação: Adolescente")
elif idade <= 59:
    print("Classificação: Adulto")
else:
    print("Classificação: Idoso")

#menu interativo com while#

opcao = ""

while opcao != "3":
    print("\n--- MENU ---")
    print("1. Soma")
    print("2. Subtração")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print(f"Resultado da Soma: {n1 + n2}")
    elif opcao == "2":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print(f"Resultado da Subtração: {n1 - n2}")
    elif opcao == "3":
        print("Saindo do programa...")
    else:
        print("Opção inválida! Tente novamente.")         