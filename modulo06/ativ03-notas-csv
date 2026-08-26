import csv


def salvar_notas(nome, nota1, nota2):
    with open("notas_alunos.csv", "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, nota1, nota2])


def carregar_notas():
    try:
        with open("notas_alunos.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            print("Notas dos Alunos (CSV):")
            for linha in leitor:
                print(f"Aluno: {linha[0]} | Nota 1: {linha[1]} | Nota 2: {linha[2]}")
    except FileNotFoundError:
        print("Nenhum arquivo de notas encontrado.")


salvar_notas("Mariana", "8.5", "9.0")
salvar_notas("Lucas", "7.0", "6.5")

carregar_notas()