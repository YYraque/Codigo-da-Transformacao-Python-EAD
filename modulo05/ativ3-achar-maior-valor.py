def maior_menor(numeros):
    maior = max(numeros)
    menor = min(numeros)
    return maior, menor

maior_valor, menor_valor = maior_menor([15, 3, 42, 8, 23])
print(f"Maior: {maior_valor}, Menor: {menor_valor}")