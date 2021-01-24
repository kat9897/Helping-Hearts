import os
import random

import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound

# change any of these constants to style and make it your own!
WINDOW_TITLE = 'Helping Hearts - a pick me up'
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800
IMG_HEIGHT = 400
IMG_WIDTH = 400
PINK_COLOR_HEX = '#dea5a4'


# opens all images from folder activity and quote
ALL_ACTIVITY = [str("activity/") + file for file in os.listdir("activity/")]
ALL_QUOTE= [str("quote/") + file for file in os.listdir("quote/")]


class selfcare:

    def __init__(self, root):
        self.root = root

        # collecting all the clothes
        self.activity_images = ALL_ACTIVITY
        self.quote_images = ALL_QUOTE

        # first pictures for top and bottom
        self.activity_image_path = self.activity_images[0]
        self.quote_image_path = self.quote_images[0]

        # creating 2 frames
        self.activity_frame = tk.Frame(self.root, bg=PINK_COLOR_HEX)
        self.quote_frame = tk.Frame(self.root, bg=PINK_COLOR_HEX)

        # adding top
        self.activity_image_label = self.create_photo(self.activity_image_path, self.activity_frame)
        self.activity_image_label.pack(side=tk.TOP)

        # adding bottom
        self.quote_image_label = self.create_photo(self.quote_image_path, self.quote_frame)
        self.quote_image_label.pack(side=tk.TOP)

        self.create_background()

    def create_background(self):
        # title and resize the window
        self.root.title(WINDOW_TITLE)
        self.root.geometry('{0}x{1}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))

        # create buttons
        self.create_buttons()

        # add the initial clothes onto the screen
        self.activity_frame.pack(fill=tk.BOTH, expand=tk.YES)
        self.quote_frame.pack(fill=tk.BOTH, expand=tk.YES)

    def create_buttons(self):
        create_combo_button = tk.Button(self.activity_frame, text="new", command=self.create_combo)
        create_combo_button.pack(side=tk.LEFT)

    def create_photo(self, image, frame):
        activity_image_file = Image.open(image)
        image = activity_image_file.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo, anchor=tk.CENTER)
        image_label.image = photo

        return image_label

    def update_photo(self, new_image, image_label):
        new_image_file = Image.open(new_image)
        image = new_image_file.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label.configure(image=photo)
        image_label.image = photo

    def create_combo(self):
        # randomly select an outfit
        new_activity_index = random.randint(0, len(self.activity_images)-1)
        new_quote_index = random.randint(0, len(self.quote_images)-1)

        # add the clothes onto the screen
        self.update_photo(self.activity_images[new_activity_index], self.activity_image_label)
        self.update_photo(self.quote_images[new_quote_index], self.quote_image_label)




if __name__ == '__main__':
    root = tk.Tk()
    app = selfcare(root)

    root.mainloop()