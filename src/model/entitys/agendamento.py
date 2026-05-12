class Agendamento:
    def __init__(self,id_agendamento:int,nome:str,data:str,hora:str,observacoes:str=""):
        self.__id_agendamento=id_agendamento
        self.__nome=nome
        self.__data=data
        self.__hora=hora
        self.observacoes=observacoes

    @property
    def id_agendamento(self):
        return self.__id_agendamento

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome=nome

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self,data):
        self.__data=data

    @property
    def hora(self):
        return self.__hora

    @hora.setter
    def hora(self,hora):
        self.__hora=hora

    @property
    def observacoes(self):
        return self.__observacoes

    @observacoes.setter
    def observacoes(self,observacoes):
        self.__observacoes=observacoes

    def __eq__(self,other):
        return self.id_agendamento==other.id_agendamento

    def agendamentoDict(self):
        return {
            "id":self.id_agendamento,
            "nome":self.nome,
            "data":self.data,
            "hora":self.hora,
            "observacoes": self.observacoes
        }

    @staticmethod
    def dict_to_object(data):
        return Agendamento(
            data["id"],
            data["nome"],
            data["data"],
            data["hora"],
            data.get("observacoes","")
    )




