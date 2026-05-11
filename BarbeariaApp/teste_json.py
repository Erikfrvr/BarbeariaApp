import json
from src.model.entitys.agendamento import Agendamento

teste=Agendamento(1,"Erik","11/05/2026","14:00","Corte favorito mid fade")

dados_para_json=teste.agendamentoDict()
print(f"Adicionado com sucesso!!! {dados_para_json}")

objeto_recuperado=Agendamento.dict_to_object(dados_para_json)
print(f"nome do cliente {objeto_recuperado.nome} hora marcada {objeto_recuperado.hora}")