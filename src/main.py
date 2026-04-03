import sys
import os

# Adiciona o diretório src ao path (para desenvolvimento)
# Adiciona o diretório atual ao path (para executável do PyInstaller)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ''))


import pygame

from core.game import Game

if __name__ == "__main__":
    game = Game()
    game.run()