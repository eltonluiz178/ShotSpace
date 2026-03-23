import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, imagePath, numberPlayer):
        super().__init__(groups)

        # Carrega imagem e dimensões do jogador
        self.image = pygame.image.load(imagePath)
        self.image = pygame.transform.scale(self.image, [60, 60])

        # Recebe posição inicial

        self.rect = pygame.Rect(400,450,60,60);

        self.numberPlayer = numberPlayer

        # Variáveis
        self.xspeed = 0
        self.xacceleration = 0.2
        self.yspeed = 0
        self.yacceleration = 0.2

    def update(self, *args):

        keys = pygame.key.get_pressed()

        if self.numberPlayer == 1:

            # Movimentação do jogador com o uso de aceleração

            if keys[pygame.K_d]:
                self.xspeed += self.xacceleration
            elif keys[pygame.K_a]:
                self.xspeed -= self.xacceleration
            elif keys[pygame.K_RIGHT]:
                self.xspeed += self.xacceleration
            elif keys[pygame.K_LEFT]:
                self.xspeed -= self.xacceleration
            else:
                self.xspeed *= 0.95

            if keys[pygame.K_w]:
                self.yspeed -= self.yacceleration
            elif keys[pygame.K_s]:
                self.yspeed += self.yacceleration
            elif keys[pygame.K_UP]:
                self.yspeed -= self.yacceleration
            elif keys[pygame.K_DOWN]:
                self.yspeed += self.yacceleration
            else:
                self.yspeed *= 0.95

            if self.xspeed > 7:
                self.xspeed = 7
            if self.yspeed > 7:
                self.yspeed = 7

            self.rect.x += self.xspeed
            self.rect.y += self.yspeed

        # Validações para impedir o jogador de sair da tela
        if self.rect.top < 0:
            self.rect.top = 0
            self.xspeed = 0
            self.yspeed = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600
            self.xspeed = 0
            self.yspeed = 0
        if self.rect.left < 0:
            self.rect.left = 0
            self.xspeed = 0
            self.yspeed = 0
        if self.rect.right > 800:
            self.rect.right = 800
            self.xspeed = 0
            self.yspeed = 0