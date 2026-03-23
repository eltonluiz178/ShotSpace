import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, imagePath, rectPlayer, numberPlayer):
        super().__init__(groups)

        # Carrega imagem e dimensões do jogador
        self.image = pygame.image.load(imagePath)
        self.image = pygame.transform.scale(self.image, [100, 100])

        # Recebe posição inicial

        self.rect = pygame.Rect(rectPlayer)

        self.numberPlayer = numberPlayer

        # Variáveis
        self.speed = 0
        self.acceleration = 0.1

    def update(self, *args):

        keys = pygame.key.get_pressed()

        if self.numberPlayer == 1:

            # Movimentação do jogador com o uso de aceleração

            if keys[pygame.K_d]:
                self.speed += self.acceleration
            elif keys[pygame.K_a]:
                self.speed -= self.acceleration
            elif keys[pygame.K_RIGHT]:
                self.speed += self.acceleration
            elif keys[pygame.K_LEFT]:
                self.speed -= self.acceleration
            else:
                self.speed *= 0.95


            self.rect.x += self.speed

        # Validações para impedir o jogador de sair da tela
        if self.rect.top < 0:
            self.rect.top = 0
            self.speed = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600
            self.speed = 0
        if self.rect.left < 0:
            self.rect.left = 0
            self.speed = 0
        if self.rect.right > 800:
            self.rect.right = 800
            self.speed = 0