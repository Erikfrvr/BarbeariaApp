import flet as ft


class AgendamentoView:
    def __init__(self):
        LARGURA_TOTAL = 400
        LARGURA_METADE = 190

        self.input_cliente = ft.TextField(
            label="Nome do Cliente",
            prefix_icon=ft.Icons.PERSON,
            border_radius=10,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(color=ft.Colors.WHITE),
            label_style=ft.TextStyle(color=ft.Colors.WHITE70),
            filled=True,
            bgcolor=ft.Colors.GREY_800,
            width=LARGURA_TOTAL,
        )

        self.input_data = ft.TextField(
            label="Data (DD/MM/AAAA)",
            prefix_icon=ft.Icons.CALENDAR_TODAY,
            border_radius=10,
            max_length=10,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(color=ft.Colors.WHITE),
            label_style=ft.TextStyle(color=ft.Colors.WHITE70),
            filled=True,
            bgcolor=ft.Colors.GREY_800,
            hint_text="Ex: 15/05/2026",
            width=LARGURA_METADE,
        )

        self.input_hora = ft.TextField(
            label="Horário (HH:MM)",
            prefix_icon=ft.Icons.ACCESS_TIME,
            border_radius=10,
            max_length=5,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(color=ft.Colors.WHITE),
            label_style=ft.TextStyle(color=ft.Colors.WHITE70),
            filled=True,
            bgcolor=ft.Colors.GREY_800,
            hint_text="Ex: 14:30",
            width=LARGURA_METADE,
        )

        self.input_servico = ft.Dropdown(
            label="Serviço",
            options=[
                ft.dropdown.Option("Corte"),
                ft.dropdown.Option("Barba"),
                ft.dropdown.Option("Corte + Barba"),
                ft.dropdown.Option("Pezinho"),
            ],
            border_radius=10,
            color=ft.Colors.WHITE,
            filled=True,
            bgcolor=ft.Colors.GREY_800,
            width=LARGURA_TOTAL,
        )

        self.input_obs = ft.TextField(
            label="Observações do Barbeiro",
            prefix_icon=ft.Icons.STICKY_NOTE_2,
            multiline=True,
            min_lines=1,
            max_lines=3,
            border_radius=10,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(color=ft.Colors.WHITE),
            label_style=ft.TextStyle(color=ft.Colors.WHITE70),
            filled=True,
            bgcolor=ft.Colors.GREY_800,
            hint_text="Ex: Cliente prefere degradê alto",
            width=LARGURA_TOTAL,
        )

        self.input_senha = ft.TextField(
            label="Senha Administrativa",
            prefix_icon=ft.Icons.LOCK,
            password=True,
            can_reveal_password=True,
            border_radius=10,
            visible=False,
            color=ft.Colors.WHITE,
            text_style=ft.TextStyle(color=ft.Colors.WHITE),
            label_style=ft.TextStyle(color=ft.Colors.WHITE70),
            filled=True,
            bgcolor=ft.Colors.GREY_800,
            width=LARGURA_TOTAL,
        )

        self.btn_agendar = ft.ElevatedButton(
            content=ft.Row(
                [
                    ft.Icon(ft.Icons.CHECK_CIRCLE, size=20),
                    ft.Text("Confirmar Agendamento", size=16),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
            ),
            bgcolor=ft.Colors.GREEN_700,
            color=ft.Colors.WHITE,
            width=LARGURA_TOTAL,
        )

        self.btn_barbeiro = ft.ElevatedButton(
            content=ft.Row(
                [
                    ft.Icon(ft.Icons.ADMIN_PANEL_SETTINGS, size=20),
                    ft.Text("Área do Barbeiro", size=16),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            bgcolor=ft.Colors.BLUE_GREY_700,
            color=ft.Colors.WHITE,
            width=LARGURA_TOTAL,
        )

        self.mensagem = ft.Text(
            value="",
            color=ft.Colors.AMBER_700,
            weight=ft.FontWeight.BOLD,
            size=15,
        )

        self.tabela = ft.DataTable(
            visible=False,
            columns=[
                ft.DataColumn(
                    ft.Text("Cliente", weight="bold", color="white")
                ),

                ft.DataColumn(
                    ft.Text("Data", weight="bold", color="white")
                ),

                ft.DataColumn(
                    ft.Text("Hora", weight="bold", color="white")
                ),

                ft.DataColumn(
                    ft.Text("Serviço", weight="bold", color="white")
                ),

                ft.DataColumn(
                    ft.Text("Observação", weight="bold", color="white")
                ),

                ft.DataColumn(
                    ft.Text("Ações", weight="bold", color="white")
                ),
            ],
            rows=[],
        )

    def build(self):
        return ft.Container(
            expand=True,
            bgcolor=ft.Colors.GREY_900,
            padding=20,
            content=ft.Column(
                scroll=ft.ScrollMode.AUTO,
                spacing=18,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[

                    ft.Icon(
                        ft.Icons.CONTENT_CUT,
                        size=55,
                        color=ft.Colors.AMBER,
                    ),

                    ft.Text(
                        "BARBEARIA APP",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE,
                    ),

                    ft.Text(
                        "Novo Agendamento",
                        size=18,
                        color=ft.Colors.WHITE70,
                    ),

                    self.input_cliente,

                    ft.Row(
                        controls=[
                            self.input_data,
                            self.input_hora
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20
                    ),

                    self.input_servico,

                    self.input_obs,

                    self.btn_agendar,

                    ft.Divider(
                        height=35,
                        color=ft.Colors.WHITE24
                    ),

                    self.btn_barbeiro,

                    self.input_senha,

                    self.mensagem,

                    self.tabela,
                ],
            ),
        )

    def addLinhaTabela(
        self,
        id,
        cliente,
        data,
        hora,
        servico,
        obs,
        on_delete
    ):

        self.tabela.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(
                        ft.Text(cliente, color="white")
                    ),

                    ft.DataCell(
                        ft.Text(data, color="white")
                    ),

                    ft.DataCell(
                        ft.Text(hora, color="white")
                    ),

                    ft.DataCell(
                        ft.Text(servico, color="white")
                    ),

                    ft.DataCell(
                        ft.Text(
                            obs if obs else "-",
                            size=12,
                            color="white70"
                        )
                    ),

                    ft.DataCell(
                        ft.IconButton(
                            ft.Icons.DELETE,
                            icon_color="red400",
                            tooltip="Excluir agendamento",
                            on_click=on_delete
                        )
                    ),
                ]
            )
        )

    def mostrarMensagem(self, texto: str):
        self.mensagem.value = texto

    def limparCampos(self):

        for field in [
            self.input_cliente,
            self.input_data,
            self.input_hora,
            self.input_obs
        ]:
            field.value = ""

        self.input_servico.value = None