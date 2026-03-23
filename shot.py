import pygame
import random

class Shot(pygame.sprite.Sprite):
    def __init__(self, imagePath,*groups):
        super().__init__(*groups)

        # Carrega imagem e dimensões do tiro

        self.image = pygame.image.load(imagePath)
        self.image = pygame.transform.scale(self.image, [20, 20])

        # Posição do disparo
        self.rect = self.image.get_rect()

        # Passa a velocidade de disparo fixa
        self.speed = 4

    def update(self, *args):
        # LOGICA
        self.rect.y -= self.speed

        # Destroi o disparo ao sair da tela
        if self.rect.top < 0:
            self.kill()