from src.views.agendamento_view import AgendamentoView
from src.controllers.agendamento_controller import AgendamentoController


def agendamento_constructor(page):

    # 1. Instancia a View (tela)
    view = AgendamentoView()

    # 2. Instancia o Controller passando page e view
    AgendamentoController(page, view)

    # 3. Retorna o layout pronto para ser desenhado
    return view.build()
