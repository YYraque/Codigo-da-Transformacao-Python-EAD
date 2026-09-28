import sys
import os
import datetime


sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from aluno import gerar_aluno
from utilidades import somar, multiplicar, calcular_media
from jogo_adivinhacao import iniciar_jogo_adivinhacao

def executar_sistema():

    
    print("--------------------------------------------------")
    print("      SISTEMA DE AVALIAÇÃO E TESTES PRÁTICOS     ")
    print("--------------------------------------------------\n")

   
    aluno = gerar_aluno()
    print("--- DADOS DO ESTUDANTE ---")
    print(f"Nome: {aluno['nome']}")
    print(f"E-mail: {aluno['email']}")
    print(f"Data de Nasc.: {aluno['data_nascimento']} ({aluno['idade']} anos)")

    # 2. Executando cálculos do teste
    print("\n--- TESTE RÁPIDO DE CÁLCULO ---")
    print(f"25 + 35 = {somar(25, 35)}")
    print(f"7 x 8 = {multiplicar(7, 8)}")

    # 3. Executando o jogo
    iniciar_jogo_adivinhacao()

    # 4. Encerramento
    agora = datetime.datetime.now()
    print(f"\nSessão finalizada em: {agora.strftime('%d/%m/%Y às %H:%M:%S')}")

if __name__ == "__main__":
    executar_sistema()