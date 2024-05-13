# Python program to take
# screenshots


import pyautogui
import tkinter as tk
from tkinter.filedialog import *
 
root = tk.Tk()
root.title("Take a Screenshot")
root.configure(bg="#37474F")

window = tk.Canvas(root, width=200, height=70, bg="#37474F")
window.pack()

def take_ss():
    screen_shot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    screen_shot.save(save_path+"_screenshot.png")
                    
ss_button= tk.Button(text="Take Screenshot",command = take_ss, font=12, bg="#C62828")
window.create_window(100,35,window=ss_button)



root.mainloop()