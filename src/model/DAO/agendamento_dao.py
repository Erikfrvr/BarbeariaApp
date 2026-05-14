import os
from .base_db import BaseDB


class Agendamento_DAO:
    def __init__(self):
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))

        caminho_db = os.path.abspath(
            os.path.join(diretorio_atual, "..", "..", "infrastructure", "database", "agendamentos.json")
        )

        self.db = BaseDB(caminho_db)

    def _gerar_id(self, agendamentos: list) -> int:
        if not agendamentos:
            return 1
        return max(a["id"] for a in agendamentos) + 1

    def addAgendamento(self, data: dict):
        if not isinstance(data, dict):
            raise ValueError("Agendamento inválido!")
        try:
            agendamentos = self.db.read()
            data["id"] = self._gerar_id(agendamentos)
            self.db.write(data)
        except Exception as e:
            print(f"Erro ao salvar agendamento: {e}")

    def lerAgendamentos(self):
        try:
            return self.db.read()
        except Exception as e:
            print(f"Erro ao ler agendamentos: {e}")
            return []

    def deletarAgendamento(self, id_agendamento: int):
        try:
            agendamentos = self.db.read()
            nova_lista = [a for a in agendamentos if a["id"] != id_agendamento]
            if len(nova_lista) == len(agendamentos):
                raise ValueError(f"Agendamento com ID {id_agendamento} não encontrado!")
            self.db.salveList(nova_lista)
        except ValueError:
            raise
        except Exception as e:
            print(f"Erro ao deletar agendamento: {e}")

    def buscarPorID(self, id: int):
        try:
            agendamentos = self.db.read()
            for a in agendamentos:
                if a["id"] == id:
                    return a
            return None
        except Exception as e:
            print(f"Erro ao buscar agendamento: {e}")
            return None

    def atualizarAgendamento(self, id_agendamento: int, novos_dados: dict):
        try:
            agendamentos = self.db.read()
            for i, a in enumerate(agendamentos):
                if a["id"] == id_agendamento:
                    agendamentos[i].update(novos_dados)
                    agendamentos[i]["id"] = id_agendamento
                    self.db.salveList(agendamentos)
                    return
            raise ValueError(f"Agendamento com ID {id_agendamento} não encontrado!")
        except ValueError:
            raise
        except Exception as e:
            print(f"Erro ao atualizar agendamento: {e}")