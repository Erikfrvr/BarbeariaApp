class ErroValue(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)

class ErroHorarioIndisponivel(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)

