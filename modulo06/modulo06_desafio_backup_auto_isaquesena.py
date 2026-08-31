import shutil
import os

def realizar_backup(pasta_origem, pasta_destino):
   
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

   
    for arquivo in os.listdir(pasta_origem):
        caminho_origem = os.path.join(pasta_origem, arquivo)
        
        
        if os.path.isfile(caminho_origem):
            shutil.copy(caminho_origem, pasta_destino)
            print(f"Arquivo '{arquivo}' copiado com sucesso!")


os.makedirs("pasta_documentos", exist_ok=True)
os.makedirs("pasta_backup", exist_ok=True)


realizar_backup("pasta_documentos", "pasta_backup")