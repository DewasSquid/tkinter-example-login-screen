import tkinter as tk
from tkinter.messagebox import showinfo, showerror
from os import system


def LoginPanel(self):
        """
        Place the login interface on the left of the screen
        Args :
            self : Instance of the parent class
        """
        canvas_login = tk.Canvas(self, background=self.palette["panel_background"], highlightthickness=0)
        canvas_login.pack(side="left", fill="y")
        
        center_frame = tk.Frame(canvas_login, background=self.palette["panel_background"])  # Used to keep the widget centered in
        center_frame.pack(expand=True)
        
        tk.Label(center_frame,
                 image=self.images_path["user_profile"], 
                 background=self.palette["panel_background"]).grid(row=0, column=0, pady=10)  # User icon on top
        
        # Entries container
        frame_entries = tk.Frame(center_frame, background=self.palette["panel_background"])  # This will contain both of the entries
        frame_entries.grid(row=1, column=0, padx=7, pady=30)
        
        # ---------------------------------------------------------------- Username entry
        user_entry_frame = tk.Frame(frame_entries)  # This will contain the username entry and icon
        user_entry_frame.grid(row=0, column=0, padx=5, pady=8)
        
        tk.Label(user_entry_frame,
                 width=62, height=55,
                 image=self.images_path["username_entry"]).grid(row=0, column=0)  # The small icon on the left
        
        entry_username = tk.Entry(user_entry_frame, font=("Calibri 12", 12), background="white", relief="flat", width=35)
        entry_username.grid(row=0, column=1, sticky="NSWE")
        
        # ---------------------------------------------------------------- Password entry
        pass_entry_frame = tk.Frame(frame_entries)  # This will contain the password entry and icon
        pass_entry_frame.grid(row=1, column=0, padx=33)
        
        tk.Label(pass_entry_frame,
                 width=62, height=55,
                 image=self.images_path["password_entry"]).grid(row=0, column=0)  # The small icon on the left
        
        entry_password = tk.Entry(pass_entry_frame, font=("Calibri 12", 12), show="*", background="white", relief="flat", width=35)
        entry_password.grid(row=0, column=1, sticky="NSWE")
        
        # ---------------------------------------------------------------- Login button
        button_login = tk.Button(center_frame, 
                                 text="LOGIN", font=("Quicksand", 15, "bold"), compound="center",
                                 image=self.images_path["proceed_button"], bd=0, relief="sunken",
                                 foreground=self.palette["proceed_button_foreground"], background=self.palette["panel_background"])
        button_login.grid(row=2, column=0, pady=27)
        
        
        def on_enter(mPos): button_login["image"] = self.images_path["proceed_button_hover"]
        def on_leave(mPos): button_login["image"] = self.images_path["proceed_button"]
        def on_click(mPos):
            button_login.config(activebackground=self.palette["panel_background"])
            on_enter(None)  # The button image doesn't show itself as hover when you don't do that
        
        button_login.bind("<Enter>", on_enter)  # Had to do this since it wont show the hover image after clicking
        button_login.bind("<Leave>", on_leave)
        button_login.bind("<Button-1>", on_click)
        
        def send_password_email():
            if not entry_username.get():
                showerror("Empty username", "Please provide a valid username.")
            else:
                showinfo("Confirm your actions", "We've send you an email to change your password.")
        
        tk.Button(center_frame, text="Forgor password ?", font=("Open Sans", 10, "italic"), relief="flat",
                  foreground=self.palette["bottom_button_foreground"], background=self.palette["panel_background"],
                  command=send_password_email).grid(row=3, column=0)  # Forgot password button
        
        
if __name__ == '__main__':
    # Launch the main file
    system("py main.py")
