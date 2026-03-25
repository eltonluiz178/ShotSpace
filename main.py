import time

import pygame
import random
import sound

from enemy import Enemy
from improvement import Improvement
from player import Player
from shot import Shot
from textSprite import TextSprite

# Variáveis
gameLoop = True

timer = 20

remainingLifes = 1

numberShots = 1

clock = pygame.time.Clock()

textRect = pygame.Rect(51,15,50,50)

# Inicializando o Pygame e criando a Janela
pygame.init()
display = pygame.display.set_mode([800, 600])
pygame.display.set_caption("ShotSpace")
icon = pygame.image.load("data/images/Rocket.png")
pygame.display.set_icon(icon)

# Groups
objectGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
improvementGroup = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()

# Background
bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("data/images/bgSpace.png")
bg.image = pygame.transform.scale(bg.image, (800, 600))
bg.rect = bg.image.get_rect()

# Objects
player = Player(objectGroup, "data/images/Rocket.png", 1)
sounds = sound.Sound()

# Sprite de vida restante
lifes = pygame.sprite.Sprite(objectGroup)
lifes.image = pygame.image.load("data/images/life.png")
lifes.image = pygame.transform.scale(lifes.image, (50, 50))
lifes.rect = pygame.Rect(0, 0, 50, 50)

quantityLifes = TextSprite(f": {remainingLifes}", 40, (35, 176, 76), textRect, objectGroup)

# Cria função com estilização do jogo
def draw():
    objectGroup.draw(display)


# Atualiza tela para continuar aberta
if __name__ == '__main__':
    while gameLoop:
        clock.tick(60)

        draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sounds.play('shot')
                    offset = 30  # distância entre os tiros

                    # garante limite de 1 a 5
                    numberShots = max(1, min(numberShots, 5))

                    # calcula ponto central
                    center_x = player.rect.centerx
                    center_y = player.rect.centery

                    for i in range(numberShots):
                        shot = Shot("data/images/Shot.png", objectGroup, shotGroup)

                        # espalha os tiros simetricamente
                        dx = (i - (numberShots - 1) / 2) * offset

                        shot.rect.center = (center_x + dx, center_y)

        objectGroup.update()

        timer += 1
        if timer > 30:
            timer = 0
            if random.random() < 0.25:
                newEnemy = Enemy("data/images/Asteroid.png", objectGroup, enemyGroup)

            if random.random() < 0.05:
                if random.random() < 0.5:
                    newImprovement = Improvement("data/images/moreShot.png", 'shot', objectGroup, improvementGroup)
                else:
                    newImprovement = Improvement("data/images/moreLife.png", 'life', objectGroup, improvementGroup)

        enemyCollisions = pygame.sprite.spritecollide(player, enemyGroup, True)

        if enemyCollisions:
            if remainingLifes == 1:
                sounds.play('fah')
                time.sleep(3)
                gameLoop = False
            else:
                remainingLifes -= 1
                quantityLifes.update_text(f": {remainingLifes}")

        improvementCollisions = pygame.sprite.spritecollide(player, improvementGroup, True)

        for improvement in improvementCollisions:
            if improvement.tipo == 'life':
                remainingLifes += 1
                quantityLifes.update_text(f": {remainingLifes}")
                sounds.play('up')
            elif improvement.tipo == 'shot':
                numberShots += 1
                sounds.play('up')

        hits = pygame.sprite.groupcollide(shotGroup, enemyGroup, True, True)


        pygame.display.update()
