#!/usr/bin/python

import pyautogui
import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from tkinter import PhotoImage
from PIL import Image, ImageTk

# Initialize the main window
root = tk.Tk()
root.title("Screenshot")
root.configure(bg="#37474F")

# Create a canvas to place widgets
window = tk.Canvas(root, width=200, height=70, bg="#1ab088", borderwidth=0)
window.pack()

# Load, resize the image to 40x40 pixels, and convert it to a format suitable for Tkinter
image_path = r"/home/jp/Applications/Screenshot/src/img/arrow.png"
original_image = Image.open(image_path)
resized_image = original_image.resize((40, 40), Image.LANCZOS)
photoimage = ImageTk.PhotoImage(resized_image)

# Define the screenshot function
def take_ss():
    screen_shot = pyautogui.screenshot()
    save_path = asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:  # Ensure the user has provided a save path
        screen_shot.save(save_path)

# Create the screenshot button
ss_button = tk.Button(root, text="Screenshot", image=photoimage, compound=tk.LEFT, command=take_ss, font=('Arial', 15), bg="#941934")
ss_button.pack(side=tk.TOP)

# Place the button on the canvas
window.create_window(100, 35, window=ss_button)

# Start the Tkinter main loop
root.mainloop()
