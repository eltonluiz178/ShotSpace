import pygame

from utils.path_helper import resource_path

class Window:
    def __init__(self, settings):
        self.settings = settings
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        pygame.display.set_caption(settings.TITLE)

        # Ícone
        try:
            icon_path = resource_path('assets/images/gameIcon.png')
            icon = pygame.image.load(icon_path)
            pygame.display.set_icon(icon)
        except:
            pass  # ícone não encontrado, continua sem ele

    def get_surface(self):
        return self.screen

    def update(self):
        pygame.display.update()