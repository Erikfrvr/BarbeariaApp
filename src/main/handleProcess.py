import flet as ft
from src.main.constructors.agendamentoConstructor import agendamento_constructor


def app(page: ft.Page):

    page.title = "Barbearia"
    page.bgcolor = ft.Colors.GREY_900
    page.scroll = ft.ScrollMode.AUTO

    def route_change(e):
        page.controls.clear()

        if page.route == "/" or page.route == "/agendamento":
            page.controls.append(agendamento_constructor(page))

        page.update()

    page.on_route_change = route_change
    page.go("/agendamento")