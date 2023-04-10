import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from copy import deepcopy, copy


class ToggleButton:
    def __init__(self, master, text, command) -> None:
        self.button = tk.Button(master, 
                                text=text)
        
        self.normal_colour = "#375a7f"
        self.pressed_colour = "#2c4866"

        self.button.config(background=self.normal_colour, 
                            activebackground=self.pressed_colour, 
                            activeforeground="white",
                            highlightbackground=self.normal_colour, 
                            command=self.get_button_function(command))
        
    def toggle(self):
        self.button.config(background=self.pressed_colour, relief="sunken")

    def untoggle(self):
        self.button.config(background=self.normal_colour, relief="flat")

    def get_button_function(self, command):
        def func(*args, **kwargs):
            command(*args, **kwargs)
            self.toggle()
            

        return func
    
    def pack(self, *args, **kwargs):
        self.button.pack(*args, **kwargs)
        
