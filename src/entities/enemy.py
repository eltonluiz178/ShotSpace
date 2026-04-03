import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, imagePath,*groups):
        super().__init__(*groups)

        # Tamanho aleatório para o asteroide
        size = random.randint(40,120)

        # Carregando imagem de forma dinâmica
        self.image = pygame.image.load(imagePath)
        self.image = pygame.transform.scale(self.image, [size, size])

        # self.rect = pygame.Rect(enemyRect)
        self.rect = pygame.Rect(0, 0, size, size)

        # Surgimento aleatório no mapa
        self.rect.y = random.randint(-400,-1)
        self.rect.x = random.randint(1,700)

        # Velociade aleatória para cada asteroide / inimigo
        self.speed = 1 + random.random() * 2

    def update(self, *args):
        # LOGICA
        self.rect.y += self.speed

        # Após passar do limite da tela é destruído
        if self.rect.bottom > 600:
            self.kill()