import json
from json import JSONDecodeError
import os


class BaseDB:
    def __init__(self, file_db:str):
# Define o caminho absoluto do banco para evitar erros de path
        diretorio_atual=os.path.dirname(os.path.abspath(__file__))
        self.__path=os.path.join(diretorio_atual, file_db)
        self.__file_db=file_db

# Inicializa o arquivo JSON caso nao exista na maquina
        if not os.path.exists(self.__path):
            with open(self.__path,"w",encoding="utf-8") as file:
                json.dump([],file)

# Leitura do JSON tratando os erros possiveis
    def read(self)->list:
        try:
            with open(self.__path,"r",encoding="utf-8") as file:
                return json.load(file)
        except JSONDecodeError:
# Retorna lista vazia caso arquivo corrompido ou vazio
            return []
        except Exception as e:
            print("Erro ao ler:",e)
            return []

# Adiciona um novo registro e preserva o anterior
    def write(self,data):
        list_data_base=self.read()
        try:
            with open(self.__path,"w",encoding="utf-8") as file:
                list_data_base.append(data)
# Salva com indentacao deixando o JSON legivel
                json.dump(list_data_base,file,ensure_ascii=False,indent=4)
        except Exception as e:
            print("Erro no salve:",e)

# Sobrescreve o banco com uma nova lista
    def salveList(self, lista):
        try:
            with open(self.__path,"w",encoding="utf-8") as file:
                json.dump(lista, file,ensure_ascii=False,indent=4)
        except Exception as e:
            print("Erro no salveList:",e)



