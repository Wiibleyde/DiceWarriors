from interface import *
from sound import MusicPlayer

if __name__=='__main__':
    music_path = "sound/sound1.mp3"
    player = MusicPlayer(music_path)
    player.play_music()
    root = tk.Tk()
    Interface(root)
    if root.mainloop() == "stop":
        player.wait_for_music_end()
        player.stop()