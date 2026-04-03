import pygame
import random
import time

from .settings import Settings
from .window import Window

# Imports das entidades e componentes
from src.entities.player import Player
from src.entities.enemy import Enemy
from src.entities.shot import Shot
from src.entities.improvement import Improvement
from src.managers.sound_manager import Sound
from src.components.textSprite import TextSprite


class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.window = Window(self.settings)
        self.clock = pygame.time.Clock()

        self.running = True

        # ====================== GRUPOS DE SPRITES ======================
        self.objectGroup = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.improvementGroup = pygame.sprite.Group()
        self.shotGroup = pygame.sprite.Group()

        # ====================== VARIÁVEIS DO JOGO ======================
        self.remainingLifes = 1
        self.numberShots = 1
        self.timer = 0
        self.last_shot = 0
        self.cooldown_shot = 700  # 0,7 segundos em ms

        # ====================== BACKGROUND ======================
        self.bg = pygame.sprite.Sprite(self.objectGroup)
        try:
            self.bg.image = pygame.image.load("assets/images/bgSpace.png")
            self.bg.image = pygame.transform.scale(self.bg.image,
                                                   (self.settings.WIDTH, self.settings.HEIGHT))
            self.bg.rect = self.bg.image.get_rect()
        except FileNotFoundError:
            print("Background 'bgSpace.png' não encontrado!")

        # ====================== PLAYER ======================
        self.player = Player(self.objectGroup, "assets/images/Rocket.png", 1)

        # ====================== SOM ======================
        self.sounds = Sound()

        # ====================== HUD - VIDAS ======================
        try:
            self.lifes_sprite = pygame.sprite.Sprite(self.objectGroup)
            self.lifes_sprite.image = pygame.image.load("assets/images/life.png")
            self.lifes_sprite.image = pygame.transform.scale(self.lifes_sprite.image, (50, 50))
            self.lifes_sprite.rect = pygame.Rect(10, 10, 50, 50)
        except FileNotFoundError:
            print("Imagem de vida não encontrada!")
            self.lifes_sprite = None

        # Texto da quantidade de vidas
        self.quantityLifes = TextSprite(
            f": {self.remainingLifes}",
            40,
            (35, 176, 76),
            pygame.Rect(65, 15, 50, 50),
            self.objectGroup
        )

        # ====================== OUTROS ======================
        self.game_over_delay = 0

    def handle_events(self):
        """Gerencia eventos do jogo (fechar janela, etc.)"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    # Spawn de aprimoramentosd
    def spawnImprovement(self, probability, enemyRect):
        if random.random() < probability:
            if random.random() < 0.5:
                newImprovement = Improvement("assets/images/moreShot.png", 'shot', enemyRect,self.objectGroup, self.improvementGroup)
            else:
                newImprovement = Improvement("assets/images/moreLife.png", 'life', enemyRect,self.objectGroup, self.improvementGroup)

    def update(self):
        """Atualiza toda a lógica do jogo"""
        keys = pygame.key.get_pressed()


        # ==================== TIRO DO JOGADOR ====================
        if keys[pygame.K_SPACE]:
            agora = pygame.time.get_ticks()

            # verifica se já passou o tempo de cooldown do tiro
            if agora - self.last_shot >= self.cooldown_shot:
                self.last_shot = agora  # atualiza o tempo do último tiro

                self.sounds.play('shot')

                offset = 30
                center_x = self.player.rect.centerx
                center_y = self.player.rect.centery

                # Limita entre 1 e 5 tiros
                self.numberShots = max(1, min(self.numberShots, 5))

                for i in range(self.numberShots):
                    shot = Shot("assets/images/Shot.png", self.objectGroup, self.shotGroup)
                    dx = (i - (self.numberShots - 1) / 2) * offset
                    shot.rect.center = (center_x + dx, center_y)

        # ==================== SPAWN DE INIMIGOS ====================
        self.timer += 1
        if self.timer > 30:
            self.timer = 0

            # Spawn de asteroides/inimigos
            if random.random() < 0.25:  # 25% de chance a cada 30 frames
                Enemy("assets/images/Asteroid.png", self.objectGroup, self.enemyGroup)

            self.spawnImprovement(0.005, None)

        # ==================== ATUALIZA TODOS OS SPRITES ====================
        self.objectGroup.update()

        # ==================== COLISÕES ====================

        # Colisão Player × Inimigo
        enemyCollisions = pygame.sprite.spritecollide(self.player, self.enemyGroup, True,
                                                      pygame.sprite.collide_mask)
        if enemyCollisions:
            if self.remainingLifes <= 1:
                self.sounds.play('fah')
                self.game_over_delay = pygame.time.get_ticks()  # inicia delay de game over
                self.remainingLifes = 0
            else:
                self.remainingLifes -= 1
                self.quantityLifes.update_text(f": {self.remainingLifes}")
                self.sounds.play('hit')  # se tiver som de hit

        # Colisão Player × Melhoria
        improvementCollisions = pygame.sprite.spritecollide(self.player, self.improvementGroup, True)
        for imp in improvementCollisions:
            if imp.tipo == 'life':
                self.remainingLifes += 1
                self.quantityLifes.update_text(f": {self.remainingLifes}")
                self.sounds.play('up')
            elif imp.tipo == 'shot':
                self.numberShots += 1
                self.sounds.play('up')

        # Colisão Tiro × Inimigo
        shotCollisions = pygame.sprite.groupcollide(self.shotGroup, self.enemyGroup, True, True,pygame.sprite.collide_mask)
        for col in shotCollisions:
            enemyRect = col.rect
            self.spawnImprovement(0.01, enemyRect)

    def draw(self):
        """Desenha tudo na tela"""
        self.objectGroup.draw(self.window.get_surface())
        self.window.update()  # pygame.display.update()

    def run(self):
        """Game Loop principal"""
        while self.running:
            self.clock.tick(self.settings.FPS)

            self.handle_events()
            self.update()
            self.draw()

            # Delay de Game Over
            if self.remainingLifes <= 0:
                if pygame.time.get_ticks() - self.game_over_delay > 3000:  # 3 segundos
                    self.running = False
                    print("Game Over!")

        # Finaliza o Pygame
        pygame.quit()