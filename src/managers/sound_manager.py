import pygame

from utils.path_helper import resource_path

class Sound():
    def __init__(self):
        # Music
        music_path = resource_path('assets/music/MusicGame.mp3')
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.08)

        # Sounds

        # Som de game over
        fah_path = resource_path('assets/sounds/Fah.mp3')
        self.fah = pygame.mixer.Sound(fah_path)
        self.fah.set_volume(0.01)

        # Som de tiro
        shot_path = resource_path('assets/sounds/Shot.wav')
        self.shot = pygame.mixer.Sound(shot_path)
        self.shot.set_volume(0.1)

        # Som de aprimoramento
        up_path = resource_path('assets/sounds/Up.mp3')
        self.up = pygame.mixer.Sound(up_path)
        self.up.set_volume(0.4)

    def play(self,name):
        if ( name == 'fah'):
            self.fah.play()
        elif ( name == 'shot'):
            self.shot.play()
        elif ( name == 'up'):
            self.up.play()