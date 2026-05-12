from datetime import datetime
from src.model.DAO.agendamento_dao import Agendamento_DAO


class AgendamentoController:

    def __init__(self,page,tela):
        self.page=page
        self.tela=tela
        self.dao=Agendamento_DAO()

        # Liga os botões da tela
        self.tela.btn_agendar.on_click=self.handleAddAgendamento

    def listarAgendamentos(self)-> None:
        agendamentos=self.dao.lerAgendamentos()
        self.tela.tabela.rows.clear()

        for ag in agendamentos:
            self.tela.addLinhaTabela(
                ag["id"],
                ag["cliente"],
                ag["data"],
                ag["hora"],
                ag["servico"],

                lambda e,id=ag["id"]: self.handleDeleteAgendamento(e,id)
            )

        self.page.update()

    def validarHorario(self,data:str,hora:str)-> bool:

        try:
            data_obj=datetime.strptime(data,"%d/%m/%Y")
        except ValueError:
            return False

        # Folga segunda-feira
        if data_obj.weekday()==0:
            return False

        # Horário de almoço (comparação por string)
        if "12:00"<=hora<"13:00":
            return False

        agendamentos=self.dao.lerAgendamentos()

        # Horário ocupado
        for ag in agendamentos:
            if ag["data"]==data and ag["hora"]==hora:
                return False

        return True

    def handleAddAgendamento(self,e):
        cliente=self.tela.input_cliente.value
        data=self.tela.input_data.value
        hora=self.tela.input_hora.value
        servico=self.tela.input_servico.value


        if not cliente or not data or not hora or not servico:
            self.tela.mostrarMensagem("Preencha todos os campos!")
            return


        try:
            data_obj=datetime.strptime(data,"%d/%m/%Y")
        except ValueError:
            self.tela.mostrarMensagem("Data inválida! Use o formato DD/MM/AAAA")
            return


        if data_obj.date()<datetime.now().date():
            self.tela.mostrarMensagem("Não é possível agendar em datas passadas!")
            return

        if data_obj.weekday()==0:
            self.tela.mostrarMensagem("Barbearia não atende às segundas-feiras!")
            return

        if not self.validarHorario(data,hora):
            self.tela.mostrarMensagem("Horário inválido, em almoço ou já ocupado!")
            return

        novo_agendamento={
            "id":int(datetime.now().timestamp()),
            "cliente":cliente,
            "data":data,
            "hora":hora,
            "servico":servico
        }
        self.dao.addAgendamento(novo_agendamento)
        self.listarAgendamentos()
        self.tela.limparCampos()

    def handleDeleteAgendamento(self,e,id_agendamento:int):
        self.dao.deletarAgendamento(id_agendamento)
        self.listarAgendamentos()

    def buscarAgendamentoID(self,id: int):
        return self.dao.buscarPorID(id)