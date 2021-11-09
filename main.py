import tkinter as tk
from tkinter.constants import SEL_LAST
from PIL import ImageTk, Image  # Used for the background wich do not work with photoImage
from panel_module import LoginPanel


class Window(tk.Tk):
    def __init__(self):
        super(Window, self).__init__()
        
        self.images_path = {
            "background": (ImageTk.PhotoImage(Image.open("assets/background.png"))),
            "user_profile": (tk.PhotoImage(file="assets/user_profile.png")),
            "username_entry": (tk.PhotoImage(file="assets/username_entry_icon.png")),
            "password_entry": (tk.PhotoImage(file="assets/password_entry_icon.png")),
            "proceed_button": (tk.PhotoImage(file="assets/panel_button_shape.png")),
            "proceed_button_hover": (tk.PhotoImage(file="assets/panel_button_hover.png"))
        }
        
        self.palette = {
            "panel_background": "#05173F",
            "proceed_button_foreground": "#DDDDDD",
            "bottom_button_foreground": "#6A6A6A",
            "panel_icon_background": "#E7E7E7"
        }
        
        bg = tk.Label(self, image=self.images_path["background"], border=0)
        bg.place(x=0, y=0)
        
        LoginPanel(self)



if __name__ == '__main__':
    win = Window()
    win.mainloop()