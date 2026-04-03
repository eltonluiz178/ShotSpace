import sys
import os


def resource_path(relative_path):
    """Obtém o caminho absoluto para o recurso, funciona tanto em desenvolvimento quanto no executável"""
    try:
        # PyInstaller cria uma variável temporária _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # Estamos em desenvolvimento
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)