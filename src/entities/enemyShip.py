import pygame
import random
from core.settings import Settings

class EnemyShip(pygame.sprite.Sprite):
    def __init__(self, imagePath,*groups):
        super().__init__(*groups)

        self.settings = Settings()

        # Tamanho da nave inimiga
        self.size = 60

        # Carregando imagem de forma dinâmica
        self.image = pygame.image.load(imagePath)
        self.image = pygame.transform.scale(self.image, [self.size, self.size])

        # self.rect = pygame.Rect(enemyRect)
        self.rect = pygame.Rect(0, 0, self.size, self.size)

        # Surgimento aleatório no mapa
        self.rect.y = random.randint(-400, -1)
        self.rect.x = random.randint(1, self.settings.WIDTH - self.size)

        # Velociade aleatória para cada inimigo
        self.speed = 1 + random.random() * 2

    def update(self, *args):
        # LOGICA
        self.rect.y += self.speed

        # Após passar do limite da tela é destruído
        if self.rect.bottom > random.randint(120, 200):
            self.speed = 0;