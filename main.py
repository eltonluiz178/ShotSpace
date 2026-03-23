import time

import pygame
import random
import sound

from enemy import Enemy
from player import Player
from shot import Shot

# Inicializando o Pygame e criando a Janela
pygame.init()
display = pygame.display.set_mode([800,600])
pygame.display.set_caption("ShotSpace")
icon = pygame.image.load("data/images/Rocket.png")
pygame.display.set_icon(icon)

# Groups
objectGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()

# Background
bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("data/images/bgSpace.png")
bg.image = pygame.transform.scale(bg.image, (800,600))
bg.rect = bg.image.get_rect()

# Objects
playerRect = pygame.Rect(400,450,100,100);
player = Player(objectGroup,"data/images/Rocket.png", playerRect,1)
sounds = sound.Sound()

# Cria função com estilização do jogo
def draw():
    display.fill([45, 45, 45])

    objectGroup.draw(display)

# Variáveis
gameLoop = True
timer = 20
clock = pygame.time.Clock()

# Atualiza tela para continuar aberta
if __name__ == '__main__':
    while gameLoop:
        clock.tick(60)

        # Evento de fechar o game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False

            # Evento de tiro do jogador
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sounds.play('shot')
                    newShot = Shot("data/images/Shot.png", objectGroup, shotGroup)
                    newShot.rect.center = player.rect.center

        objectGroup.update()

        # Geração aleatória de inimigos com 30% de chance
        timer += 1
        if timer > 30:
            timer = 0
            if random.random() < 0.3:
                newEnemy = Enemy("data/images/Asteroid.png", objectGroup, enemyGroup)


        # Colisão de jogador com inimigo encerra game
        collisions = pygame.sprite.spritecollide(player, enemyGroup, False)

        if collisions:
            sounds.play('fah')
            time.sleep(3)
            gameLoop = False

        # Disparo do jogador destrói inimigo

        hits = pygame.sprite.groupcollide(shotGroup, enemyGroup, True, True)

        draw()
        pygame.display.update()