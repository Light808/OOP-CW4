import tkinter as tk
import video_library as lib
import tkinter.messagebox as msgbox

class UpdateVideos():
    def __init__(self, window):
        window.geometry("400x250")
        window.title("Update Video Rating")

        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.video_id_txt = tk.Entry(window, width=10)
        self.video_id_txt.grid(row=0, column=1, padx=10, pady=10)

        enter_rating_lbl = tk.Label(window, text="Enter New Rating")
        enter_rating_lbl.grid(row=1, column=0, padx=10, pady=10)

        self.new_rating_txt = tk.Entry(window, width=10)
        self.new_rating_txt.grid(row=1, column=1, padx=10, pady=10)

        update_rating_btn = tk.Button(window, text="Update Rating", command=self.update_rating)
        update_rating_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=2, sticky="W", padx=10, pady=10)


    def update_rating(self):
        video_id = self.video_id_txt.get()
        new_rating = self.new_rating_txt.get()
        try:
            new_rating = int(new_rating)
        except ValueError:
            self.status_lbl.configure(text="Rating must be an integer!")
            return
        if new_rating >5 or new_rating<0:
            return self.status_lbl.configure(text="Rating must be in range of 1-5 !")
        if lib.update_rating(video_id, new_rating):
            name = lib.get_name(video_id)
            play_count = lib.get_play_count(video_id)
            self.status_lbl.configure(text=f"{name} updated to rating {new_rating}, play count {play_count}")
        else:
            self.status_lbl.configure(text="Error updating video rating!")

if __name__ == "__main__":
    window = tk.Tk()
    app = UpdateVideos(window)
    window.mainloop()