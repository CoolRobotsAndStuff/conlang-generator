import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from toggle_button import ToggleButton
from characteristic import CharacteristicStack


class StackEditor:
    def __init__(self, master) -> None:
        self.frame = ttk.Frame(master)
        self.stack = CharacteristicStack()

        self.stack_name_text = ttk.StringVar()

        self.stack_name_label = ttk.Label(self.frame, textvariable=self.stack_name_text, font=("Arial", 30))
        self.characteristics_label = ttk.Label(self.frame, text="Characteristics", justify=LEFT, font=("Arial", 15))

        self.characteristics_frame = tk.Frame(self.frame)
        self.characteristics_frame.config(bg="#444444")

        self.characteristic_buttons = []


    def delete_all_buttons(self):
        for item in self.characteristics_frame.winfo_children():
            item.destroy()

    def set_stack(self, name, stack: CharacteristicStack):
        self.stack_name_text.set(name.capitalize())
        self.stack = stack
        print(self.stack.get_string())

        self.delete_all_buttons()
        self.characteristic_buttons = []
        for char in self.stack.members:
            button = ToggleButton(self.characteristics_frame, char, lambda : 0)
            button.pack(side=TOP, pady=5, fill=X, padx=5)
            self.characteristic_buttons.append(button)

    def pack(self, *args, **kwargs):
        self.stack_name_label.pack(side=TOP, anchor=NW, padx=20, pady=10)
        self.characteristics_label.pack(side=TOP, anchor=NW, padx=20)
        self.characteristics_frame.pack(side=TOP, fill=BOTH, padx=20)