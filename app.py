import flet as ft
import ssl
from src.main.handleProcess import app

ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == "__main__":
    ft.run(app)