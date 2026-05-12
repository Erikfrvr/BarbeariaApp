from datetime import datetime
from src.model.DAO.agendamento_dao import Agendamento_DAO

SENHA_BARBEIRO="1234"


class AgendamentoController:

    def __init__(self,page,tela):

        self.page=page
        self.tela=tela
        self.dao=Agendamento_DAO()

        # BOTÕES
        self.tela.btn_agendar.on_click = self.handleAddAgendamento
        self.tela.btn_barbeiro.on_click = self.handleAcessoBarbeiro


    #LISTA DE AGENDAMENTO

    def listarAgendamentos(self) -> None:

        agendamentos=self.dao.lerAgendamentos()
        self.tela.tabela.rows.clear()

        for ag in agendamentos:

            self.tela.addLinhaTabela(
                ag["id"],
                ag["cliente"],
                ag["data"],
                ag["hora"],
                ag["servico"],

                lambda e,id=ag["id"]:
                self.handleDeleteAgendamento(e,id)
            )

        self.page.update()

    # VALIDAR HORÁRIO

    def validarHorario(self,data:str,hora:str)-> bool:

        try:
            data_obj=datetime.strptime(data, "%d/%m/%Y")

        except ValueError:
            return False

        # SEGUNDA-FEIRA FECHADO
        if data_obj.weekday()==0:
            return False

        # HORÁRIO DE ALMOÇO
        if "12:00"<=hora<"13:00":
            return False

        agendamentos=self.dao.lerAgendamentos()

        # HORÁRIO OCUPADO
        for ag in agendamentos:

            if ag["data"]==data and ag["hora"]==hora:
                return False

        return True

    # ADICIONAR AGENDAMENTO
    def handleAddAgendamento(self,e):

        cliente = self.tela.input_cliente.value
        data = self.tela.input_data.value
        hora = self.tela.input_hora.value
        servico = self.tela.input_servico.value

        if not cliente or not data or not hora or not servico:

            self.tela.mostrarMensagem("Preencha todos os campos!")
            return

        try:
            data_obj=datetime.strptime(data, "%d/%m/%Y")

        except ValueError:

            self.tela.mostrarMensagem(
                "Data inválida! Use DD/MM/AAAA"
            )
            return

        # DATA PASSADA
        if data_obj.date()<datetime.now().date():

            self.tela.mostrarMensagem(
                "Não é possível agendar em datas passadas!"
            )
            return

        # SEGUNDA
        if data_obj.weekday()==0:

            self.tela.mostrarMensagem(
                "Barbearia não atende às segundas!"
            )
            return

        # VALIDA HORÁRIO
        if not self.validarHorario(data,hora):

            self.tela.mostrarMensagem(
                "Horário inválido ou ocupado!"
            )
            return

        novo_agendamento={

            "id": int(datetime.now().timestamp()),
            "cliente":cliente,
            "data":data,
            "hora":hora,
            "servico":servico
        }

        self.dao.addAgendamento(novo_agendamento)

        self.listarAgendamentos()

        self.tela.limparCampos()

        self.tela.mostrarMensagem("Agendamento realizado!")

    # DELETAR AGENDAMENTO

    def handleDeleteAgendamento(self,e,id_agendamento: int):

        self.dao.deletarAgendamento(id_agendamento)
        self.listarAgendamentos()

    # BUSCAR POR ID

    def buscarAgendamentoID(self,id:int):

        return self.dao.buscarPorID(id)

    # ACESSO BARBEIRO

    def handleAcessoBarbeiro(self, e):

        senha=self.tela.input_senha.value

        # mostra campo senha se ainda estiver vazio
        if not senha:

            self.tela.input_senha.visible = True
            self.tela.mostrarMensagem(
                "Digite a senha do barbeiro!"
            )

            self.page.update()
            return

        # valida senha
        if senha==SENHA_BARBEIRO:

            self.tela.tabela.visible=True
            self.listarAgendamentos()

            self.tela.mostrarMensagem(
                "Acesso liberado!"
            )

        else:

            self.tela.mostrarMensagem(
                "Senha incorreta!"
            )

        self.page.update()