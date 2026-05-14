from datetime import datetime, timedelta
from src.model.DAO.agendamento_dao import Agendamento_DAO

SENHA_BARBEIRO = "1234"


class AgendamentoController:
    def __init__(self, page, tela):
        self.page = page
        self.tela = tela
        self.dao = Agendamento_DAO()

        self.tela.btn_agendar.on_click = self.handleAddAgendamento
        self.tela.btn_barbeiro.on_click = self.handleAcessoBarbeiro

        self.tela.input_data.on_change = self.aplicar_mascara_data
        self.tela.input_hora.on_change = self.aplicar_mascara_hora

    def aplicar_mascara_data(self, e):
        val = e.control.value
        if len(val) in [2, 5]:
            if not val.endswith("/"):
                e.control.value += "/"
        self.page.update()

    def aplicar_mascara_hora(self, e):
        val = e.control.value
        if len(val) == 2:
            if not val.endswith(":"):
                e.control.value += ":"
        self.page.update()

    def validar_regras_negocio(self, data_str, hora_str):
        try:
            data_obj = datetime.strptime(data_str, "%d/%m/%Y")
            hoje = datetime.now()
        except ValueError:
            return "Formato de data inválido."

        if data_obj.date() < hoje.date():
            return "Não é possível agendar em datas retroativas."

        limite = hoje + timedelta(days=60)
        if data_obj > limite:
            return "Agendamentos permitidos apenas para os próximos 60 dias."

        if data_obj.weekday() == 0:
            return "A barbearia não abre às segundas-feiras."

        if "12:00" <= hora_str < "13:00":
            return "Horário de almoço indisponível."

        agendamentos = self.dao.lerAgendamentos()
        for ag in agendamentos:
            if ag["data"] == data_str and ag["hora"] == hora_str:
                return "Este horário já está ocupado por outro cliente."

        return None

    def handleAddAgendamento(self, e):
        cliente = self.tela.input_cliente.value
        data = self.tela.input_data.value
        hora = self.tela.input_hora.value
        servico = self.tela.input_servico.value
        obs = self.tela.input_obs.value

        if not all([cliente, data, hora, servico]):
            self.tela.mostrarMensagem("Por favor, preencha todos os campos obrigatórios.")
            self.page.update()
            return

        erro = self.validar_regras_negocio(data, hora)
        if erro:
            self.tela.mostrarMensagem(erro)
            self.page.update()
            return

        novo_agendamento = {
            "cliente": cliente,
            "data": data,
            "hora": hora,
            "servico": servico,
            "obs": obs
        }

        self.dao.addAgendamento(novo_agendamento)
        self.tela.limparCampos()
        self.tela.mostrarMensagem("Sucesso! Agendamento confirmado.")

        if self.tela.tabela.visible:
            self.listarAgendamentos()

        self.page.update()

    def handleAcessoBarbeiro(self, e):
        senha = self.tela.input_senha.value

        if not self.tela.input_senha.visible:
            self.tela.input_senha.visible = True
            self.tela.mostrarMensagem("Digite a senha administrativa.")
            self.page.update()
            return

        if senha == SENHA_BARBEIRO:
            self.tela.tabela.visible = True
            self.listarAgendamentos()
            self.tela.mostrarMensagem("Acesso administrativo liberado.")
            self.tela.input_senha.value = ""
        else:
            self.tela.mostrarMensagem("Senha incorreta.")

        self.page.update()

    def listarAgendamentos(self):
        if not self.tela.tabela.visible:
            return

        agendamentos = self.dao.lerAgendamentos()
        self.tela.tabela.rows.clear()

        for ag in agendamentos:
            self.tela.addLinhaTabela(
                ag["id"],
                ag["cliente"],
                ag["data"],
                ag["hora"],
                ag["servico"],
                ag.get("obs", ""),
                lambda e, id_ag=ag["id"]: self.handleDelete(e, id_ag)
            )
        self.page.update()

    def handleDelete(self, e, id_ag):
        self.dao.deletarAgendamento(id_ag)
        self.listarAgendamentos()