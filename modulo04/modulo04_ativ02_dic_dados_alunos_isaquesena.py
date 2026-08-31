aluno = {
    "nome": "Lucas Silva",
    "idade": 17,
    "notas": [8.5, 7.0, 9.2]
}

print("--- DADOS DO ALUNO ---")
print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']} anos")
print(f"Notas: {', '.join(map(str, aluno['notas']))}")

media = sum(aluno["notas"]) / len(aluno["notas"])
print(f"Média: {media:.2f}")