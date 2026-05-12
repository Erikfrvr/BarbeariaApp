from flet import *


class ServicoView(View):

    def __init__(self):
        super().__init__()

        # Campos
        self.nomeServico = TextField(
            label="Nome do Serviço",
            prefix_icon=Icons.PERSON,
            col=7
        )

        self.marcaServico = TextField(
            label="Marca",
            prefix_icon=CupertinoIcons.CUBE_BOX_FILL,
            col=7
        )

        self.valorServico = TextField(
            label="Valor",
            prefix="R$",
            col=3
        )

        self.btnCadastrarServico = ElevatedButton(
            text="Adicionar",
            icon=CupertinoIcons.PLUS
        )

        # Tabela
        self.tabelaServico = DataTable(
            columns=[
                DataColumn(label=Text("ID")),
                DataColumn(label=Text("Nome")),
                DataColumn(label=Text("Marca")),
                DataColumn(label=Text("Valor R$")),
            ]
        )

        self.route = "/servicos"

    def build(self):

        modalServico = Container(
            content=Column(
                controls=[
                    ResponsiveRow(
                        controls=[
                            self.nomeServico,
                            self.valorServico
                        ],
                        alignment=MainAxisAlignment.SPACE_AROUND
                    ),

                    ResponsiveRow(
                        controls=[
                            self.marcaServico,
                            self.btnCadastrarServico
                        ],
                        alignment=MainAxisAlignment.SPACE_AROUND
                    ),
                ]
            ),
            padding=10,
            border=border.all(2, "#E9EEF6"),
            height=160,
            col=12
        )

        modalTabela = Container(
            content=ResponsiveRow(
                controls=[self.tabelaServico],
                alignment=MainAxisAlignment.CENTER
            ),
            padding=padding.all(10)
        )

        return [
            Column(
                controls=[
                    modalServico,
                    modalTabela
                ]
            )
        ]