import tkinter as tk
from tkinter import filedialog
import pygame
import librosa

class AudioPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Player")

        self.y, sr = librosa.load(librosa.ex('trumpet'))

        # Create buttons for opening, playing, pausing, and resuming audio files
        # self.open_button = tk.Button(root, text="Open Audio File", command=self.open_audio)
        self.play_button = tk.Button(root, text="Play", state=tk.NORMAL, command=self.play_audio)
        self.pause_button = tk.Button(root, text="Pause", state=tk.DISABLED, command=self.pause_audio)
        self.resume_button = tk.Button(root, text="Resume", state=tk.DISABLED, command=self.resume_audio)

        # self.open_button.pack(pady=10)
        self.play_button.pack()
        self.pause_button.pack()
        self.resume_button.pack()

        # Initialize pygame
        pygame.mixer.init()

        # Register a callback to stop audio when the window is closed
        root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Initialize playback state
        self.paused = False

    # def open_audio(self):
    #     file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    #     if file_path:
    #         self.audio_file = file_path
    #         self.play_button.config(state=tk.NORMAL)

    def play_audio(self):
        pygame.mixer.music.load(self.y)
        pygame.mixer.music.play()
        self.play_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)

    def pause_audio(self):
        pygame.mixer.music.pause()
        self.pause_button.config(state=tk.DISABLED)
        self.resume_button.config(state=tk.NORMAL)
        self.paused = True

    def resume_audio(self):
        pygame.mixer.music.unpause()
        self.resume_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.paused = False

    def on_closing(self):
        # Check if audio is currently playing
        if pygame.mixer.music.get_busy():
            # Stop audio playback before closing the application
            pygame.mixer.music.stop()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioPlayerApp(root)
    root.mainloop()
