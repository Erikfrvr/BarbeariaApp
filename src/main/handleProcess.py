from flet import *
from src.views.servicoView import ServicoView


def app(page: Page):

    page.title = "Sistema Barbearia"

    def changeRoutes(route):

        page.views.clear()

        if page.route == "/":
            page.views.append(
                ServicoView()
            )

        page.update()

    page.on_route_change = changeRoutes

    page.go("/")