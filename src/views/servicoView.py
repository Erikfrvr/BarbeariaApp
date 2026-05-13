import flet as ft

class ServicoView:

    def __init__(self):
        self.nomeServico = ft.TextField(
            label="Nome do Serviço",
            prefix_icon=ft.Icons.PERSON,
            col=7
        )
        self.marcaServico = ft.TextField(
            label="Marca",
            col=7
        )
        self.valorServico = ft.TextField(
            label="Valor",
            prefix="R$",
            col=3
        )
        self.btnCadastrarServico = ft.ElevatedButton(
            text="Adicionar",
            icon=ft.Icons.ADD
        )
        self.tabelaServico = ft.DataTable(
            columns=[
                ft.DataColumn(label=ft.Text("ID")),
                ft.DataColumn(label=ft.Text("Nome")),
                ft.DataColumn(label=ft.Text("Marca")),
                ft.DataColumn(label=ft.Text("Valor R$")),
            ],
            rows=[]
        )

    def build(self):
        modalServico = ft.Container(
            content=ft.Column(
                controls=[
                    ft.ResponsiveRow(
                        controls=[self.nomeServico, self.valorServico],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND
                    ),
                    ft.ResponsiveRow(
                        controls=[self.marcaServico, self.btnCadastrarServico],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND
                    ),
                ]
            ),
            padding=10,
            border=ft.border.all(2, "#E9EEF6"),
            height=160,
        )

        modalTabela = ft.Container(
            content=ft.ResponsiveRow(
                controls=[self.tabelaServico],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            padding=ft.padding.all(10)
        )

        return ft.Column(
            controls=[modalServico, modalTabela]
        )