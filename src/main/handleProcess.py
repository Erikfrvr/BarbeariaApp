import flet as ft


class AgendamentoView:

    def __init__(self):

        # ── INPUTS CLIENTE ─────────────────────────────
        self.input_cliente = ft.TextField(
            label="Seu Nome",
            prefix_icon=ft.Icons.PERSON,
            border_radius=10,
            expand=True,
        )

        self.input_data = ft.TextField(
            label="Data (DD/MM/AAAA)",
            prefix_icon=ft.Icons.CALENDAR_TODAY,
            border_radius=10,
            expand=True,
        )

        self.input_hora = ft.TextField(
            label="Horário (HH:MM)",
            prefix_icon=ft.Icons.ACCESS_TIME,
            border_radius=10,
            expand=True,
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
        )

        # ── SENHA BARBEIRO ─────────────────────────────
        self.input_senha = ft.TextField(
            label="Senha do Barbeiro",
            prefix_icon=ft.Icons.LOCK,
            password=True,
            can_reveal_password=True,
            border_radius=10,
            visible=False,
            expand=True,
        )

        # ── BOTÕES ─────────────────────────────
        self.btn_agendar = ft.ElevatedButton(
            text="Confirmar Agendamento",
            icon=ft.Icons.CHECK_CIRCLE,
        )

        self.btn_barbeiro = ft.ElevatedButton(
            text="Entrar como Barbeiro",
            icon=ft.Icons.ADMIN_PANEL_SETTINGS,
        )

        # ── MENSAGEM ─────────────────────────────
        self.mensagem = ft.Text(
            value="",
            color=ft.Colors.AMBER_700,
            weight=ft.FontWeight.BOLD,
        )

        # ── TABELA ─────────────────────────────
        self.tabela = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Cliente")),
                ft.DataColumn(ft.Text("Data")),
                ft.DataColumn(ft.Text("Hora")),
                ft.DataColumn(ft.Text("Serviço")),
            ],
            rows=[],
        )

    # ─────────────────────────────────────────────
    # BUILD (ÚNICO E CORRETO)
    # ─────────────────────────────────────────────
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
                    self.mensagem,

                    self.tabela,
                ],
            ),
        )

    # ─────────────────────────────────────────────
    # MÉTODOS AUXILIARES
    # ─────────────────────────────────────────────
    def mostrarMensagem(self, texto: str):
        self.mensagem.value = texto

    def limparCampos(self):
        self.input_cliente.value = ""
        self.input_data.value = ""
        self.input_hora.value = ""
        self.input_servico.value = None

    def addLinhaTabela(self, id, cliente, data, hora, servico):
        self.tabela.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(id))),
                    ft.DataCell(ft.Text(cliente)),
                    ft.DataCell(ft.Text(data)),
                    ft.DataCell(ft.Text(hora)),
                    ft.DataCell(ft.Text(servico)),
                ]
            )
        )