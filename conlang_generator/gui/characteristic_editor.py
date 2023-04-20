import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from gui.toggle_button import ToggleButton
from backend.characteristic import SimpleCharacteristic


class CharacteristicEditor:
    def __init__(self, master) -> None:
        self.frame = ttk.Frame(master)
        self.chracterisic = SimpleCharacteristic

        self.characteristic_name_text = ttk.StringVar()
        self.characteristc_name_label = ttk.Label(self.frame, textvariable=self.characteristic_name_text, font=("Arial", 30))

    def delete_all(self):
        for item in self.frame.winfo_children():
            item.destroy()

    def set_characteristic(self, item):
        name, characteristic = item
        print("setting characteristic:", name.capitalize())
        self.characteristic_name_text.set(name.capitalize())
        self.chracterisic = characteristic
        #self.delete_all()

    def pack(self, *args, **kwargs):
        self.characteristc_name_label.pack(side=TOP, anchor=NW, padx=20, pady=10)
        #self.frame.pack(side=TOP, fill=BOTH, padx=20)