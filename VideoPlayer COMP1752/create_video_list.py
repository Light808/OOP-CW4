import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib
from play_playlist import PlayPlaylist 

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", content)

class CreateVideoList:
    def __init__(self, window):
        self.playlist = []

        window.geometry("1000x600")
        window.title("Create Video List")

        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=10)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)

        add_video_btn = tk.Button(window, text="Add to Playlist", command=self.add_to_playlist)
        add_video_btn.grid(row=0, column=2, padx=10, pady=10)

        play_playlist_btn = tk.Button(window, text="Play Playlist", command=self.play_playlist)
        play_playlist_btn.grid(row=0, column=3, padx=10, pady=10)

        reset_playlist_btn = tk.Button(window, text="Reset Playlist", command=self.reset_playlist)
        reset_playlist_btn.grid(row=0, column=4, padx=10, pady=10)

        random_video_btn = tk.Button(window, text="Random Video", command=self.add_random_video)
        random_video_btn.grid(row=0, column=5, padx=10, pady=10)

        self.playlist_txt = tkst.ScrolledText(window, width=70, height=20, wrap="none")
        self.playlist_txt.grid(row=1, column=0, columnspan=7, padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=7, sticky="W", padx=10, pady=10)

    def add_to_playlist(self):
        video_id = self.input_txt.get()
        name = lib.get_name(video_id)
        if name:
            if video_id not in self.playlist:
                self.playlist.append(video_id)
                self.update_playlist_display()
                self.status_lbl.configure(text=f"Added video {video_id} to playlist!")
            else:
                self.status_lbl.configure(text=f"Video {video_id} is already in the playlist!")
        else:
            self.status_lbl.configure(text=f"Video {video_id} not found!")

    def add_random_video(self):
        video_id = lib.get_random_video_id()
        if video_id:
            if video_id not in self.playlist:
                self.input_txt.delete(0, tk.END)  
                self.input_txt.insert(0, video_id) 
                self.playlist.append(video_id)
                self.update_playlist_display()
                self.status_lbl.configure(text=f"Added random video {video_id} to playlist!")
            else:
                self.status_lbl.configure(text=f"Random video {video_id} is already in the playlist!")
        else:
            self.status_lbl.configure(text="No random video found!")

    def update_playlist_display(self):
        playlist_names = [lib.get_name(video_id) for video_id in self.playlist]
        set_text(self.playlist_txt, "\n".join(playlist_names))

    def play_playlist(self):
        if self.playlist: 
            for video_id in self.playlist:
                lib.increment_play_count(video_id)
            self.update_playlist_display()
            PlayPlaylist(self.playlist_txt)
        else:
            self.status_lbl.configure(text="There are no videos in the playlist.")

    def reset_playlist(self):
        self.playlist = []
        set_text(self.playlist_txt, "")
        self.status_lbl.configure(text="Playlist reset.")

if __name__ == "__main__":
    window = tk.Tk()
    app = CreateVideoList(window)
    window.mainloop()
