import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from gui.toggle_button import ToggleButton
from backend.characteristic import CharacteristicStack, SimpleCharacteristic


class StackEditor:
    def __init__(self, master, selected_item_callback) -> None:
        self.frame = ttk.Frame(master)
        self.stack = CharacteristicStack()

        self.stack_name_text = ttk.StringVar()

        self.stack_name_label = ttk.Label(self.frame, textvariable=self.stack_name_text, font=("Arial", 30))
        self.characteristics_label = ttk.Label(self.frame, text="Characteristics", justify=LEFT, font=("Arial", 15))

        self.characteristics_frame = tk.Frame(self.frame)
        self.characteristics_frame.config(bg="#444444")

        self.characteristic_buttons = []

        self.current_characteristic = SimpleCharacteristic()
        self.current_characteristic_name = "none"

        self.selected_item_callback = selected_item_callback

    def get_select_item_function(self, item):
        def select_item():
            self.selected_item = item
            self.selected_item_callback(item)
            self.untoggle_all_buttons()
            print("set selected item to", item)
        return select_item

    def delete_all_buttons(self):
        for item in self.characteristics_frame.winfo_children():
            item.destroy()
    
    def untoggle_all_buttons(self):
        for item in self.characteristic_buttons:
            item.untoggle()

    def set_stack(self, name, stack: CharacteristicStack):
        self.stack_name_text.set(name.capitalize())
        self.stack = stack
        print(self.stack.get_string())

        self.delete_all_buttons()
        self.characteristic_buttons = []
        for char in self.stack.members:
            item = (char, self.stack.members[char])
            button = ToggleButton(master=self.characteristics_frame, text=char, command=self.get_select_item_function(item))
            button.pack(side=TOP, pady=5, fill=X, padx=5)
            self.characteristic_buttons.append(button)

        
        self.selected_item_callback(("Not selected", SimpleCharacteristic()))


    def pack(self, *args, **kwargs):
        self.stack_name_label.pack(side=TOP, anchor=NW, padx=20, pady=10)
        self.characteristics_label.pack(side=TOP, anchor=NW, padx=20)
        self.characteristics_frame.pack(side=TOP, fill=BOTH, padx=20)