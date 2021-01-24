import os
import random

import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound
import tkinter.font as font
ALL_ACTIVITY = [str("activity/") + file for file in os.listdir("activity/")] # opens all images from folder activity and quote
ALL_QUOTE= [str("quote/") + file for file in os.listdir("quote/")]

class selfcare:
    def __init__(self, root):
        self.root = root
        self.activity_images = ALL_ACTIVITY
        self.quote_images = ALL_QUOTE
        # first pictures
        self.activity_image_path = self.activity_images[0]
        self.quote_image_path = self.quote_images[0]
        # 2 frames to display quote + actvitity 
        self.activity_frame = tk.Frame(self.root, bg='#dea5a4')
        self.quote_frame = tk.Frame(self.root, bg='#dea5a4')
        # add the activity 
        self.activity_image_label = self.create_photo(self.activity_image_path, self.activity_frame)
        self.activity_image_label.pack(side=tk.TOP)
        # add the quote 
        self.quote_image_label = self.create_photo(self.quote_image_path, self.quote_frame)
        self.quote_image_label.pack(side=tk.TOP)
        self.create_background()

    def create_background(self):
        self.root.title('Helping Hearts - a pick me up')
        self.root.geometry('{0}x{1}'.format(500, 850))
        self.create_buttons()
        self.activity_frame.pack(fill=tk.BOTH, expand=tk.YES) #quote/activity on to screen
        self.quote_frame.pack(fill=tk.BOTH, expand=tk.YES)

    def create_buttons(self):
        create_combo_button = tk.Button(self.activity_frame, text="new", command=self.create_combo)
        create_combo_button.pack(side=tk.LEFT)

    def create_photo(self, image, frame):
        activity_image_file = Image.open(image)
        image = activity_image_file.resize((400, 400), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo, anchor=tk.CENTER)
        image_label.image = photo
        return image_label

    def update_photo(self, new_image, image_label):
        new_image_file = Image.open(new_image)
        image = new_image_file.resize((400, 400), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label.configure(image=photo)
        image_label.image = photo

    def create_combo(self):
        # randomly select a combination 
        new_activity_index = random.randint(0, len(self.activity_images)-1)
        new_quote_index = random.randint(0, len(self.quote_images)-1)
        # add them on to the screen
        self.update_photo(self.activity_images[new_activity_index], self.activity_image_label)
        self.update_photo(self.quote_images[new_quote_index], self.quote_image_label)

if __name__ == '__main__':
    root = tk.Tk()
    app = selfcare(root)
    root.mainloop()
