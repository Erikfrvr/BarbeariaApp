from src.model.base_db import BaseDB

class Agendamento_DAO:
    def __init__(self):
        #conecta com o arquivo agendamento.json
        self.db=BaseDB("agendamento.json")

    def addAgendamento(self,data:dict):
        agendamentos=self.db.read()
        agendamentos.append(data)
        self.db.weite(agendamentos)

    def lerAgendamentos(self):
        return self.db.read()

    def deletarAgendamento(self,id_agendamento:int):
        agendamentos=self.db.read()
        nova_lista=[a for a in agendamentos if a["id"] !=id_agendamento]
        self.db.weite(nova_lista)

    def buscarPorID(self,id:int):
        agendamentos=self.db.read()
        for a in agendamentos:
            if a ["id"]==id:
                return a
