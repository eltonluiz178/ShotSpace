import pygame

class Sound():
    def __init__(self):
        # Music
        pygame.mixer.music.load("assets/music/MusicGame.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.08)

        # Sounds

        # Som de game over
        self.fah = pygame.mixer.Sound("assets/sounds/Fah.mp3")
        self.fah.set_volume(0.01)

        # Som de tiro
        self.shot = pygame.mixer.Sound("assets/sounds/Shot.wav")
        self.shot.set_volume(0.1)

        # Som de aprimoramento
        self.up = pygame.mixer.Sound("assets/sounds/Up.mp3")
        self.up.set_volume(0.4)

    def play(self,name):
        if ( name == 'fah'):
            self.fah.play()
        elif ( name == 'shot'):
            self.shot.play()
        elif ( name == 'up'):
            self.up.play()