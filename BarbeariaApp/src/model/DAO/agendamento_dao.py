from src.model.base_db import BaseDB

class Agendamento_DAO:
    def __init__(self):
        # conecta com o arquivo agendamento.json
        self.db = BaseDB("agendamento.json")

    def addAgendamento(self,data:dict):

        if not isinstance(data,dict):
            raise ValueError("Agendamento inválido!")

        try:
            agendamentos=self.db.read()
            agendamentos.append(data)
            self.db.write(agendamentos)
        except Exception as e:
            print(f"Erro ao salvar agendamento: {e}")

    def lerAgendamentos(self):

        try:
            return self.db.read()
        except Exception as e:
            print(f"Erro ao ler agendamentos: {e}")
            return []

    def deletarAgendamento(self,id_agendamento:int):
        try:
            agendamentos=self.db.read()
            nova_lista=[a for a in agendamentos if a["id"] != id_agendamento]

            # avisa se o ID não foi encontrado
            if len(nova_lista)==len(agendamentos):
                raise ValueError(f"Agendamento com ID {id_agendamento} não encontrado!")

            self.db.write(nova_lista)
        except ValueError:
            raise
        except Exception as e:
            print(f"Erro ao deletar agendamento: {e}")

    def buscarPorID(self,id:int):
        try:
            agendamentos=self.db.read()
            for a in agendamentos:
                if a["id"]==id:
                    return a
            return None
        except Exception as e:
            print(f"Erro ao buscar agendamento: {e}")
            return None