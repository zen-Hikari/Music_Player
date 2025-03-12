import os
import pygame
import tkinter as tk
from tkinter import filedialog, PhotoImage
from PIL import Image, ImageTk
from mutagen.mp3 import MP3

pygame.mixer.init()

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x600")
        self.root.configure(bg="#f0f0f0")

        self.current_song = ""
        self.playlist = []
        self.song_index = 0
        self.is_playing = False
        self.is_rotating = False
        self.rotation_angle = 0
        self.is_seeking = False  

        # Frame utama
        self.main_frame = tk.Frame(root, bg="#f0f0f0")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Gambar Vinyl
        self.original_vinyl_image = Image.open("icons/vinyl.png").resize((190, 190), Image.LANCZOS)
        self.vinyl_photo = ImageTk.PhotoImage(self.original_vinyl_image)
        self.vinyl_label = tk.Label(self.main_frame, image=self.vinyl_photo, bg="#f0f0f0")
        self.vinyl_label.pack(pady=40)

        # Judul lagu
        self.song_title = tk.Label(self.main_frame, text="", font=("Poppins", 12, "bold"), fg="black", bg="#f0f0f0")
        self.song_title.pack(pady=5)

        # Frame Progress Bar
        self.progress_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.current_time_label = tk.Label(self.progress_frame, text="0:00", font=("Poppins", 10), bg="#f0f0f0")
        self.current_time_label.grid(row=0, column=0, padx=5)
        self.progress = tk.Scale(self.progress_frame, from_=0, to=100, orient="horizontal", length=250, 
                                 bg="#e0e0e0", sliderlength=10, showvalue=0, bd=0, 
                                 troughcolor="#d0d0d0", highlightthickness=0)
        self.progress.grid(row=0, column=1)
        self.progress.bind("<Button-1>", self.start_seek)  
        self.progress.bind("<ButtonRelease-1>", self.end_seek)  
        self.total_time_label = tk.Label(self.progress_frame, text="0:00", font=("Poppins", 10), bg="#f0f0f0")
        self.total_time_label.grid(row=0, column=2, padx=5)
        self.progress_frame.pack_forget()  

        # Tombol Load Music
        self.load_button = tk.Button(self.main_frame, text="Load Folder", command=self.load_music_folder, 
                                     fg="black", font=("Poppins", 12, "bold"), width=15, bg="#e0e0e0", relief="solid")
        self.load_button.pack(pady=5)

        # Frame tombol kontrol
        self.controls_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.controls_frame.pack(pady=5)

        self.prev_img = PhotoImage(file="icons/prev.png")
        self.play_img = PhotoImage(file="icons/play.png")
        self.pause_img = PhotoImage(file="icons/pause.png")
        self.next_img = PhotoImage(file="icons/next.png")

        self.prev_button = tk.Button(self.controls_frame, image=self.prev_img, command=self.prev_song, bg="#f0f0f0", borderwidth=0)
        self.prev_button.grid(row=0, column=0, padx=8)

        self.play_button = tk.Button(self.controls_frame, image=self.play_img, command=self.toggle_play_pause, bg="#f0f0f0", borderwidth=0)
        self.play_button.grid(row=0, column=1, padx=8)

        self.next_button = tk.Button(self.controls_frame, image=self.next_img, command=self.next_song, bg="#f0f0f0", borderwidth=0)
        self.next_button.grid(row=0, column=2, padx=8)

    def load_music_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.playlist = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".mp3")]
            if self.playlist:
                self.song_index = 0
                self.current_song = self.playlist[self.song_index]
                self.song_title.config(text=os.path.basename(self.current_song))
                self.play_song()

    def play_song(self):
        if self.current_song:
            pygame.mixer.music.load(self.current_song)
            pygame.mixer.music.play()
            self.is_playing = True
            self.play_button.config(image=self.pause_img)
            self.is_rotating = True
            self.rotate_vinyl()
            self.progress_frame.pack()
            self.update_progress()

    def prev_song(self):
        if self.playlist:
            self.song_index = (self.song_index - 1) % len(self.playlist)
            self.current_song = self.playlist[self.song_index]
            self.song_title.config(text=os.path.basename(self.current_song))
            self.play_song()

    def next_song(self):
        if self.playlist:
            self.song_index = (self.song_index + 1) % len(self.playlist)
            self.current_song = self.playlist[self.song_index]
            self.song_title.config(text=os.path.basename(self.current_song))
            self.play_song()

    def toggle_play_pause(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False
            self.play_button.config(image=self.play_img)
            self.is_rotating = False
        else:
            pygame.mixer.music.unpause()
            self.is_playing = True
            self.play_button.config(image=self.pause_img)
            self.is_rotating = True
            self.rotate_vinyl()

    def update_progress(self):
        if self.is_playing and not self.is_seeking:  
            try:
                audio = MP3(self.current_song)
                song_length = audio.info.length
                current_time = pygame.mixer.music.get_pos() / 1000
                progress_value = int((current_time / song_length) * 100)
                self.progress.set(progress_value)
                self.current_time_label.config(text=f"{int(current_time // 60)}:{int(current_time % 60):02}")
                self.total_time_label.config(text=f"{int(song_length // 60)}:{int(song_length % 60):02}")
            except:
                pass
        self.root.after(1000, self.update_progress)

    def start_seek(self, event):
        self.is_seeking = True
        pygame.mixer.music.pause()

    def end_seek(self, event):
        if self.current_song:
            self.is_seeking = False
            audio = MP3(self.current_song)
            song_length = audio.info.length
            seek_time = (self.progress.get() / 100) * song_length
            pygame.mixer.music.set_pos(seek_time)  # Update posisi lagu setelah seek
            pygame.mixer.music.unpause()
            self.is_playing = True
            self.play_button.config(image=self.pause_img)

    def rotate_vinyl(self):
        if not self.is_rotating:
            return
        self.rotation_angle = (self.rotation_angle - 3) % 360
        rotated_image = self.original_vinyl_image.rotate(self.rotation_angle, resample=Image.BICUBIC)
        self.vinyl_photo = ImageTk.PhotoImage(rotated_image)
        self.vinyl_label.config(image=self.vinyl_photo)
        self.root.after(30, self.rotate_vinyl)

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
