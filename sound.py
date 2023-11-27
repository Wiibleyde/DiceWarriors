import pygame
import time

class MusicPlayer:
    def __init__(self, music_path):
        pygame.init()
        self.music_path = music_path

    def play_music(self):
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.play()

    def wait_for_music_end(self):
        while pygame.mixer.music.get_busy():
            time.sleep(1)

    def stop(self):
        pygame.quit()

if __name__ == "__main__":
    # Remplacez "chemin/vers/votre/musique.mp3" par le chemin réel de votre fichier MP3.
    music_path = "sound/sound1.mp3"

    player = MusicPlayer(music_path)
    player.play_music()
    player.wait_for_music_end()
    player.stop()
