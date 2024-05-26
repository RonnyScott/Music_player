import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x150")
        
        # Initialize Pygame mixer
        pygame.mixer.init()

        # Track whether music is playing
        self.playing = False

        # Load button
        self.load_button = tk.Button(self.root, text="Load", command=self.load_music)
        self.load_button.pack(pady=10)

        # Play/Pause button
        self.play_pause_button = tk.Button(self.root, text="Play/Pause", command=self.play_pause_music)
        self.play_pause_button.pack(pady=10)

        # Stop button
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=10)

    def load_music(self):
        self.music_file = filedialog.askopenfilename(filetypes=[("Music Files", "*.mp3 *.wav")])
        if self.music_file:
            pygame.mixer.music.load(self.music_file)
            self.playing = False

    def play_pause_music(self):
        if not self.playing:
            pygame.mixer.music.play()
            self.playing = True
        else:
            pygame.mixer.music.pause()
            self.playing = False

    def stop_music(self):
        pygame.mixer.music.stop()
        self.playing = False

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
