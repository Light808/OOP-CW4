import tkinter as tk
import create_video_list as CreateVideoList
import font_manager as fonts
from check_videos import CheckVideos
from update_videos import UpdateVideos
import tkinter.messagebox as msgbox

def check_videos_clicked():
    status_lbl.configure(text="Check Videos button was clicked!")
    CheckVideos(tk.Toplevel(window))

def create_videos_list_clicked():
    status_lbl.configure(text="Create Videos List button was clicked!")
    CreateVideoList.CreateVideoList(tk.Toplevel(window))

def update_videos_clicked():
    status_lbl.configure(text="Update Videos button was clicked!")
    UpdateVideos(tk.Toplevel(window))

def shutdown_btn():
    msgbox.showinfo("Self Destruct", "OH Perry look like you found out my Self-Destruct Button, Wait don't press it Perry. Nooooo.....")
    window.destroy()

def toggle_mode():
    global dark_mode  
    if dark_mode:
        apply_light_mode()
        toggle_mode_btn.configure(text="Dark Mode")
    else:
        apply_dark_mode()
        toggle_mode_btn.configure(text="Light Mode")
    dark_mode = not dark_mode  

def apply_dark_mode():
    window.configure(bg="#333333")
    status_lbl.configure(bg="#333333", fg="#FFFFFF")
    header_lbl.configure(bg="#333333", fg="#FFFFFF")
    for widget in window.winfo_children():
        if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
            widget.configure(bg="#333333", fg="#FFFFFF")

def apply_light_mode():
    window.configure(bg="#FFFFFF")
    status_lbl.configure(bg="#FFFFFF", fg="#000000")
    header_lbl.configure(bg="#FFFFFF", fg="#000000")
    for widget in window.winfo_children():
        if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
            widget.configure(bg="#FFFFFF", fg="#000000")

window = tk.Tk()
window.geometry("520x250")
window.title("Video Player")

fonts.configure()

dark_mode = False


header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")
header_lbl.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

check_videos_btn = tk.Button(window, text="Check Videos", command=check_videos_clicked)
check_videos_btn.grid(row=1, column=0, padx=10, pady=10)

create_video_list_btn = tk.Button(window, text="Create Video List", command=create_videos_list_clicked)
create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)

update_videos_btn = tk.Button(window, text="Update Videos", command=update_videos_clicked)
update_videos_btn.grid(row=1, column=2, padx=10, pady=10)

shutdown_button = tk.Button(window, text="Self-destruct Button", command=shutdown_btn)
shutdown_button.grid(row=1, column=5, padx=10, pady=10)

toggle_mode_btn = tk.Button(window, text="Dark Mode", command=toggle_mode)
toggle_mode_btn.place(relx=0.0, rely=1.0, anchor='sw', x=10, y=-10)

status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
status_lbl.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

window.mainloop()