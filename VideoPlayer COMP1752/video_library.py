import random
class LibraryItem:
    def __init__(self, name, director, rating, play_count=0):
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = play_count

library = {}
library["01"] = LibraryItem("Tom and Jerry", "Fred Quimby", 4)
library["02"] = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5)
library["03"] = LibraryItem("Casablanca", "Michael Curtiz", 2)
library["04"] = LibraryItem("The Sound of Music", "Robert Wise", 1)
library["05"] = LibraryItem("Gone with the Wind", "Victor Fleming", 3)

def get_name(video_id):
    item = library.get(video_id)
    return item.name if item else None

def get_director(video_id):
    item = library.get(video_id)
    return item.director if item else None

def get_rating(video_id):
    item = library.get(video_id)
    return item.rating if item else None

def get_play_count(video_id):
    item = library.get(video_id)
    return item.play_count if item else None

def list_all():
    return "\n".join(f"{key}: {val.name}" for key, val in library.items())

def add_video(video_id, name, director, rating, play_count=0):
    if video_id not in library:
        library[video_id] = LibraryItem(name, director, rating, play_count)
        return True
    return False

def increment_play_count(video_id):
    if video_id in library:
        library[video_id].play_count += 1

def update_rating(video_id, new_rating):
    if video_id in library:
        library[video_id].rating = new_rating
        return True
    return False

def get_random_video_id():
    return random.choice(list(library.keys()))