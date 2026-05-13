import json
from json import JSONDecodeError
import os


class GeradorID:
    def __init__(self,path_file,atributo):
# Pega a pasta atual do script e acha a pasta database
        diretorio_atual=os.path.dirname(os.path.abspath(__file__))
        pasta_database=os.path.join(os.path.dirname(diretorio_atual),"database")
        self.path_file=os.path.join(pasta_database,path_file)
        self.id_gerado=None

        try:
# Le o arquivo json de agendamentos
            with open(self.path_file,"r",encoding="utf-8") as file:
                lista=json.load(file)

# Cria uma lista separada so com os IDs que ja existem
                lista_ids=[]
                for item in lista:
                    lista_ids.append(item[atributo])

# pega o maior id dessa lista paa usar no novo cliente
                self.id_gerado=max(lista_ids)

        except (JSONDecodeError,FileNotFoundError):
# Se nao achar o arquivo ou der erro, o id comeca no 1
            self.id_gerado=1
