from datetime import datetime
from src.model.DAO.agendamento_dao import Agendamento_DAO


class AgendamentoController:

    def __init__(self, page,tela):
        self.page=page
        self.tela=tela
        self.dao=Agendamento_DAO

        #liga o boatao da tela
        self.tela.btn_agendar.on_click=self.handleAddAgendamento

    def listarAgendamentos(self)->None:
        agendamentos=self.dao.lerAgendamentos()
        self.tela.tabela.rows.clear()

        for ag in agendamentos:
            self.tela.addLinhaTabela(
                ag["id"],
                ag["cliente"],
                ag["data"],
                ag["hora"],
                ag["servico"]

            )
            self.page.update()

    def validarHorario(self,data:str,hora:str)-> bool:
        data_obj=datetime.strptime(data,"%d/%m/%y")

        #folga segunda feira
        if data_obj.weekday()==0:
            return False
        #horario de almoço
        if "12:00"<=hora<"13:00":
            return False

        agendamentos=self.dao.lerAgendamentos()


        #horario ocupado
        for ag in agendamentos:
            if ag["data"]==data and ag ["hora"]==hora:
                return False

        return True


    def handleAddAgendamento (self,e):
        cliente=self.tela.input_cliente.value
        data=self.tela.input_data.value
        hora=self.tela.input_hora.value
        servico=self.tela.input_servico.value

        data_obj=datetime.strptime(data,"%d/%m/%y")

        #mensagem da segunda
        if data_obj.mostrarMensagem("Barbearia não atende às segundas-feiras!"):
            return

        if not self.validarHorario(data,hora):
            self.tela.mostrarMensagem("Horário inválido, em almoço ou já ocupado!")
            return

        novo_agendamento={
            "id": int(datetime.now().timestamp()),
            "cliente": cliente,
            "data": data,
            "hora": hora,
            "servico": servico
        }
        self.dao.addAgendamento(novo_agendamento)
        self.listarAgendamentos()
        self.tela.limparCampos()

    def handleDeleteAgendamento(self,e,id_agendamento:int):
        self.dao.deletarAgendamento(id_agendamento)
        self.listarAgendamentos()

    def buscarAgendamentoID(self,id:int):
        return self.dao.buscarPorID(id)















