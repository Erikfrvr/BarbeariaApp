import json
from json import JSONDecodeError
import os

class GeradorID:
    def __init__(self,path_file,atributo):
# acha a pasta database subindo um diretorio
        diretorio_atual=os.path.dirname(os.path.abspath(__file__))
        pasta_database=os.path.join(os.path.dirname(diretorio_atual), "database")
        self.path_file=os.path.join(pasta_database, path_file)

        self.id_gerado=None

        try:
# le o arquivo pra ver o que ja tem salvo
            with open(self.path_file,"r",encoding="utf-8") as file:
                lista = json.load(file)

# se a lista tiver vazia o comando max() buga, entao comeca no 1
                if len(lista)==0:
                    self.id_gerado=1
                else:
# separa os ids que ja existem e soma 1 no maior pra nao dar conflito
                    lista_ids=[]
                    for item in lista:
                        lista_ids.append(item[atributo])

                    self.id_gerado=max(lista_ids)+1

        except (JSONDecodeError,FileNotFoundError):
# plano B: se o arquivo nao existir ou der erro na leitura, o id vira 1
            self.id_gerado=1
