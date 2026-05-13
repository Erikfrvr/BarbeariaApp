import json
import os
from src.infrastructure.services.geradorID import GeradorID

def testar_gerador():
    print("Iniciando teste")
    arquivo="banco_teste.json"

# pega o caminho do arquivo gerado pelo sistema pra usar nos testes
    caminho_db=GeradorID(arquivo,"id").path_file

# teste 1: json vazio (simulando o primeiro uso do app)
    with open(caminho_db,"w") as f:
        json.dump([],f)

    try:
        teste_vazio = GeradorID(arquivo,"id")
        print(f"Teste 1 (Lista Vazia) - Sucesso! ID gerado:{teste_vazio.id_gerado}")
    except Exception as e:
        print(f"Teste 1 - Erro ao lidar com lista vazia: {e}")

# teste 2: adiciona um registro pra ver se o incremento do id funciona
    with open(caminho_db,"w") as f:
        json.dump([{"id": 1,"nome": "Cliente Teste"}],f)

    try:
        teste_populado=GeradorID(arquivo,"id")
        if teste_populado.id_gerado==2:
            print(f"Teste 2 (Incremento) - Sucesso! ID gerado:{teste_populado.id_gerado}")
        else:
            print(f"Teste 2 - Falha. Gerou ID:{teste_populado.id_gerado},mas esperava 2.")
    except Exception as e:
        print(f"Teste 2 - Erro na leitura do ID: {e}")

# apaga o arquivo temporario pra nao ficar lixo no projeto
    if os.path.exists(caminho_db):
        os.remove(caminho_db)
    print("Fim do teste")

if __name__ == "__main__":
    testar_gerador()