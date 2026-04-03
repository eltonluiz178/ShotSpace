import pygame
import random
from ..core.settings import Settings

class Improvement(pygame.sprite.Sprite):
    def __init__(self, imagePath, tipo,*groups):
        super().__init__(*groups)

        self.settings = Settings()

        # Carregando imagem de forma dinâmica
        self.image = pygame.image.load(imagePath)
        self.image = pygame.transform.scale(self.image, [40, 40])

        # Posição inicial
        self.rect = pygame.Rect(0, 0, 100, 100)

        # Surgimento aleatório no mapa
        self.rect.y = random.randint(-400,-1)
        self.rect.x = random.randint(1,self.settings.WIDTH - 100)

        self.tipo = tipo

        # Velociade aleatória para cada aprimoramento
        self.speed = 1 + random.random() * 2

    def update(self, *args):
        # LOGICA
        self.rect.y += self.speed

        # Após passar do limite da tela é destruído
        if self.rect.bottom > self.settings.HEIGHT:
            self.kill()