import tkinter as tk
import os
import random
from PIL import Image, ImageTk

class PlayPlaylist:
    def __init__(self, window):
        self.play_window = tk.Toplevel(window)
        self.play_window.title("Play Playlist")

        self.img_label = tk.Label(self.play_window)
        self.img_label.pack(pady=20)

        self.toggle_btn = tk.Button(self.play_window, text="Stop Slideshow", command=self.toggle_slideshow)
        self.toggle_btn.pack(pady=10)

        self.image_list = self.get_image_list(os.path.dirname(__file__)) 

        self.slideshow_running = True
        self.image_timer = None

        self.display_random_image()

    def get_image_list(self, image_directory):
        return [os.path.join(image_directory, file) for file in os.listdir(image_directory) if file.endswith('.png')]

    def display_random_image(self):
        if self.image_list:
            image_path = random.choice(self.image_list)

            img = Image.open(image_path)
            img = img.resize((300, 300), Image.LANCZOS)  
            img = ImageTk.PhotoImage(img)

            self.img_label.configure(image=img)
            self.img_label.image = img  

            if self.slideshow_running:
                self.image_timer = self.play_window.after(4000, self.display_random_image)

    def toggle_slideshow(self):
        if self.slideshow_running:
            self.slideshow_running = False
            if self.image_timer:
                self.play_window.after_cancel(self.image_timer)
            self.toggle_btn.configure(text="Start Slideshow")
        else:
            self.slideshow_running = True
            self.display_random_image()
            self.toggle_btn.configure(text="Stop Slideshow")

if __name__ == "__main__":
    window = tk.Tk()
    window.withdraw()  
    PlayPlaylist(window)
    window.mainloop()
