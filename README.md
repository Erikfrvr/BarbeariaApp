# BarbeariaApp 

Sistema de agendamento e gerenciamento para barbearias, desenvolvido em Python. O grande foco desse projeto foi aplicar a arquitetura **MVC (Model-View-Controller)**. 
Mas o que isso significa na prática? Nós dividimos o sistema em três camadas totalmente independentes:
* **Model (Modelo/Dados):** É o cofre do sistema. Cuida apenas da estrutura dos dados e de salvar as informações no nosso arquivo JSON.
* **View (Visão/Telas):** É a vitrine. São as telas, botões e formulários feitos no Flet. É tudo aquilo que o usuário vê e clica.
* **Controller (Controlador/Regras):** É o meio de campo. Ele recebe a ação da tela (View), verifica as regras (como checar se o horário está livre) e manda salvar no banco (Model).

A grande vantagem de usar o MVC é que se precisarmos mudar a cor de um botão na tela, não corremos o risco de estragar a lógica de agendamento ou apagar os dados do banco, porque tudo está separado!

## O que o app faz?
O sistema atende tanto o cliente quanto o dono da barbearia:
* **Área do Cliente:** Formulário simples onde o cliente digita o nome, escolhe a data e agenda o horário do corte.
* **Área do Barbeiro:** Um painel de gestão com uma tabela (Data Table) mostrando todos os horários marcados. O barbeiro pode excluir agendamentos e adicionar observações (ex: "cliente prefere degradê na zero").

**Regras de Negócio (O diferencial):** O sistema é blindado contra bagunça na agenda. Se o cliente tentar marcar um corte no horário de almoço do barbeiro (12h às 13h) ou escolher um horário que outro cliente já pegou, o app bloqueia a ação na hora e exibe um erro na tela.

## Tecnologias Usadas
* **Python** (Lógica principal)
* **Flet** (Para construir a interface gráfica e janelas)
* **JSON** (Banco de dados local para persistência das informações)
  

## Como rodar o projeto no seu PC
1. Faça o clone deste repositório.
2. É recomendado criar e ativar um ambiente virtual (`.venv`).
3. Instale a biblioteca do Flet (ou use o requirements):
   `pip install flet`
4. Rode o arquivo principal do projeto:
   `python app.py`

## Equipe Desenvolvedora
Dividimos o projeto em 3 frentes para trabalhar em paralelo sem gerar conflito no código:
* **Erik:** Estrutura de banco de dados, arquivos JSON e Entidades (Model).
* **Daiane:** Lógicas de bloqueio, validações de horário e persistência (Controller e DAO).
* **Lyss:** Interface gráfica, navegação e formulários usando Flet (View e Main).
