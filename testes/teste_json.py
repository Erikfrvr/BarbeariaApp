import json
from src.model.entitys.agendamento import Agendamento

teste=Agendamento(1,"Erik","11/05/2026","14:00","Corte favorito mid fade")

dados_para_json=teste.agendamentoDict()
print(f"Adicionado com sucesso!!! {dados_para_json}")

objeto_recuperado=Agendamento.dict_to_object(dados_para_json)
print(f"nome do cliente {objeto_recuperado.nome} hora marcada {objeto_recuperado.hora}")


from src.model.DAO.agendamento_dao import Agendamento_DAO

dao = Agendamento_DAO()

# ── TESTE 1: Adicionar ──────────────────────────────
print("=== ADICIONANDO ===")
dao.addAgendamento({"nome": "João", "horario": "10:00"})
dao.addAgendamento({"nome": "Maria", "horario": "11:00"})

# ── TESTE 2: Ler todos ──────────────────────────────
print("\n=== LENDO TODOS ===")
agendamentos = dao.lerAgendamentos()
print(agendamentos)

# ── TESTE 3: Buscar por ID ──────────────────────────
print("\n=== BUSCANDO ID 1 ===")
resultado = dao.buscarPorID(1)
print(resultado)

# ── TESTE 4: Atualizar ──────────────────────────────
print("\n=== ATUALIZANDO ID 1 ===")
dao.atualizarAgendamento(1, {"horario": "14:00"})
print(dao.buscarPorID(1))

# ── TESTE 5: Deletar ────────────────────────────────
print("\n=== DELETANDO ID 1 ===")
dao.deletarAgendamento(1)
print(dao.lerAgendamentos())

# ── TESTE 6: Buscar ID que não existe ───────────────
print("\n=== BUSCANDO ID QUE NÃO EXISTE ===")
print(dao.buscarPorID(999))