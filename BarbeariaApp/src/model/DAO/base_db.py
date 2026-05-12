import json
from json import JSONDecodeError
import os


class BaseDB:
    def __init__(self, file_db:str):
        # Define o caminho absoluto do banco para evitar erros de path
        diretorio_atual=os.path.dirname(os.path.abspath(__file__))
        self.__path=os.path.join(diretorio_atual, file_db)
        self.__file_db=file_db

