import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts


def set_text(text_area, content): # Define a method that set the content of text
  
    # Deletes all text from the given text_area from the start ("1.0") to the end (tk.END)
    text_area.delete("1.0", tk.END)
  
    # Inserts the given content into the text_area at the beginning (1.0)
    text_area.insert(1.0, content)

class CheckVideos(): #Create a class for CheckVideos
    def __init__(self, window):# Define a method to initialize the class with the 'window' parameter
       
        # Sets the size of the window to 750x350 pixels
        window.geometry("750x350")
       
        # Sets the title of the window to "Check Videos"
        window.title("Check Videos")

        # Creates a button to list all videos and assigns its callback method
        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
      
        # Places the button in the grid layout at row 0, column 0 with padding
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        # Creates a label prompting the user to enter a video number
        enter_lbl = tk.Label(window, text="Enter Video Number")
      
        # Places the label in the grid layout at row 0, column 1 with padding
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Creates an entry widget for inputting video numbers
        self.input_txt = tk.Entry(window, width=3)
      
        # Places the entry widget in the grid layout at row 0, column 2 with padding
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Creates a button to check video details and assigns its callback method
        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
      
        # Places the button in the grid layout at row 0, column 3 with padding
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        # Creates a scrolled text widget to list all videos
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
       
        # Places the scrolled text widget in the grid layout at row 1, column 0 spanning 3 columns with padding
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Creates a text widget to display details of a selected video
        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")
       
        # Places the text widget in the grid layout at row 1, column 3 with padding
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # Creates a label to display status messages
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
       
        # Places the status label in the grid layout at row 2, column 0 spanning 4 columns with padding
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Calls the method to list all videos when initializing
        self.list_videos_clicked()

    def check_video_clicked(self):# Define a method that handles the event check_video_clicked
       
        # Retrieves the video number entered by the user
        key = self.input_txt.get()
       
        # Gets the name of the video from the library using the entered key
        name = lib.get_name(key)

        if name is not None: # When the condition is met with the if statement do the below
         
            # If the video is found, get its director, rating, and play count from the library
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
           
            # Format the video details for display
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
          
            # Set the formatted video details in the video text widget
            set_text(self.video_txt, video_details)
        else: #if the condition not met the if part above so go to this 

            # If the video is not found, display a not found message
            set_text(self.video_txt, f"Video {key} not found")
       
        # Update the status label to indicate the button was clicked
        self.status_lbl.configure(text="Check Video button was clicked!")

    def list_videos_clicked(self):# Define a method that handles the event when list_videos_clicked
       
        # Retrieves the list of all videos from the library
        video_list = lib.list_all()
       
        # Set the list of all videos in the list text widget
        set_text(self.list_txt, video_list)
        
        # Update the status label to indicate the button was clicked
        self.status_lbl.configure(text="List Videos button was clicked!")

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    CheckVideos(window)     # open the CheckVideo GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
