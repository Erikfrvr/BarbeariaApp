import flet as ft


class AgendamentoView:

    def __init__(self):

        self.input_cliente = ft.TextField(
            label="Seu Nome",
            prefix_icon=ft.Icons.PERSON,
            border_radius=10,
            expand=True,
            color=ft.Colors.WHITE,
            label_style=ft.TextStyle(color=ft.Colors.WHITE70),
        )

        self.input_data = ft.TextField(
            label="Data (DD/MM/AAAA)",
            prefix_icon=ft.Icons.CALENDAR_TODAY,
            border_radius=10,
            expand=True,
            color=ft.Colors.WHITE,
            label_style=ft.TextStyle(color=ft.Colors.WHITE70),
        )

        self.input_hora = ft.TextField(
            label="Horário (HH:MM)",
            prefix_icon=ft.Icons.ACCESS_TIME,
            border_radius=10,
            expand=True,
            color=ft.Colors.WHITE,
            label_style=ft.TextStyle(color=ft.Colors.WHITE70),
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
            expand=True,
            color=ft.Colors.WHITE,
            label_style=ft.TextStyle(color=ft.Colors.WHITE70),
        )

        self.input_senha = ft.TextField(
            label="Senha do Barbeiro",
            prefix_icon=ft.Icons.LOCK,
            password=True,
            can_reveal_password=True,
            border_radius=10,
            visible=False,
            expand=True,
            color=ft.Colors.WHITE,
            label_style=ft.TextStyle(color=ft.Colors.WHITE70),
        )

        self.btn_agendar = ft.ElevatedButton(
            content=ft.Row([
                ft.Icon(ft.Icons.CHECK_CIRCLE),
                ft.Text("Confirmar Agendamento"),
            ])
        )

        self.btn_barbeiro = ft.ElevatedButton(
            content=ft.Row([
                ft.Icon(ft.Icons.ADMIN_PANEL_SETTINGS),
                ft.Text("Entrar como Barbeiro"),
            ])
        )

        self.mensagem = ft.Text(
            value="",
            color=ft.Colors.AMBER_700,
            weight=ft.FontWeight.BOLD,
        )

        self.tabela = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID", color=ft.Colors.WHITE)),
                ft.DataColumn(ft.Text("Cliente", color=ft.Colors.WHITE)),
                ft.DataColumn(ft.Text("Data", color=ft.Colors.WHITE)),
                ft.DataColumn(ft.Text("Hora", color=ft.Colors.WHITE)),
                ft.DataColumn(ft.Text("Serviço", color=ft.Colors.WHITE)),
                ft.DataColumn(ft.Text("Ação", color=ft.Colors.WHITE)),
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
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        "AGENDAMENTO FUNCIONANDO",
                        color=ft.Colors.WHITE,
                        size=28,
                        weight=ft.FontWeight.BOLD,
                    ),
                    self.input_cliente,
                    ft.Row([self.input_data, self.input_hora]),
                    self.input_servico,
                    self.btn_agendar,
                    ft.Divider(),
                    ft.Text(
                        "Área Barbeiro",
                        color=ft.Colors.WHITE,
                        size=18,
                    ),
                    self.btn_barbeiro,
                    self.input_senha,
                    self.mensagem,
                    self.tabela,
                ],
            ),
        )

    def mostrarMensagem(self, texto: str):
        self.mensagem.value = texto

    def limparCampos(self):
        self.input_cliente.value = ""
        self.input_data.value = ""
        self.input_hora.value = ""
        self.input_servico.value = None

    def addLinhaTabela(self, id, cliente, data, hora, servico, on_delete):
        self.tabela.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(id), color=ft.Colors.WHITE)),
                    ft.DataCell(ft.Text(cliente, color=ft.Colors.WHITE)),
                    ft.DataCell(ft.Text(data, color=ft.Colors.WHITE)),
                    ft.DataCell(ft.Text(hora, color=ft.Colors.WHITE)),
                    ft.DataCell(ft.Text(servico, color=ft.Colors.WHITE)),
                    ft.DataCell(
                        ft.IconButton(
                            icon=ft.Icons.DELETE,
                            icon_color=ft.Colors.RED_400,
                            on_click=on_delete,
                        )
                    ),
                ]
            )
        )