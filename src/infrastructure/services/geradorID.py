import json
from json import JSONDecodeError
import os


class GeradorID:
    def __init__(self, path_file, atributo):
# Pega a pasta atual do script e acha a pasta database
        diretorio_atual=os.path.dirname(os.path.abspath(__file__))
        pasta_database=os.path.join(os.path.dirname(diretorio_atual),"database")
        self.path_file=os.path.join(pasta_database,path_file)
        self.id_gerado=None

