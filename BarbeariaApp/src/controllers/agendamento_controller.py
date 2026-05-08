

from datetime import datetime

class Agendamentocontroller:
    def __init__(self,page,tela):
        self.page=page
        self.tela=tela
        self.dao=Agendamento_DAO()

        self.tela.btn_agendar.on_click=self.handleAddAgendamento

    def listarAgendamentos(self)->None:
        agendamentos=self.dao.lerAgendamentos()
        self.tela.tabela.rows.clear()

        for ag in agendamentos:
            self.tela.addLinhaabela(
                ag["id"],
                ag["cliente"],
                ag["data"],
                ag["hora"],
                ag["servico"]
            )
        self.page.update()

    def validarHorario(self,data:str,hora:str)->bool:
        data_obj=datetime.strptime(data, "%d/%m/%y")

        if data_obj.weekday()==0:
            return False

        if "12:00"<= hora<"13:00":
            return False
        agendamentos=self.dao.lerAgendamentos()

        for ag in agendamentos:
            if ag["data"]==data and ag["hora"]==hora:
                return False

        return True

    def handleAddAgendamento (self,e):
        cliete=self.tela.input_cliente.value
        data=self.tela.input_data.value
        hora=self.tela.input_hora.value
        servico=self.tela.input_servico.value

        data_obj=datetime.strptime(data,"%d/%m/%y")
        oi=1

