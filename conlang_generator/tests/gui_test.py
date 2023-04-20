import tkinter as tk

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from gui.searcher import Searcher
from gui.stack_editor import StackEditor
from gui.characteristic_editor import CharacteristicEditor

from backend.characteristic import ComplexCharacteristic, SimpleCharacteristic, CharacteristicStack
from backend.characteristics.sufix import Sufix



# Root
root = ttk.Window(themename="darkly")
root.geometry("400x400")
root.title("Conlang creator")

# Tabs
tab_control = ttk.Notebook(root)

#Stacks
stacks_tab = ttk.PanedWindow(tab_control, orient=HORIZONTAL)

my_stacks = {
    "verb":CharacteristicStack(),
    "noun":CharacteristicStack(),
    "adverb":CharacteristicStack()
}

gender = ComplexCharacteristic("")
gender.add_variant("femenino", Sufix({"sufix":"a"}))
gender.add_variant("masculino", Sufix({"sufix":"o"}))

number = ComplexCharacteristic("singular")
number.add_variant("singular", SimpleCharacteristic())
number.add_variant("plural", Sufix({"sufix":"o"}))

my_stacks["noun"].insert_item(1, "gender", gender)
my_stacks["noun"].insert_item(1, "number", number)


characteristic_editor = CharacteristicEditor(stacks_tab)

stack_editor = StackEditor(stacks_tab, characteristic_editor.set_characteristic)

def show_searched_characteristic(item):
    stack_editor.set_stack(item[0], item[1])

stack_searcher = Searcher(stacks_tab, my_stacks, show_searched_characteristic)

stacks_tab.add(stack_searcher.frame)
stacks_tab.add(stack_editor.frame)
stacks_tab.add(characteristic_editor.frame)

stacks_tab.pack()

stack_searcher.pack()
stack_editor.pack()
characteristic_editor.pack()


words_tab =  ttk.Frame(tab_control)

tab_control.add(stacks_tab, text="Characteristic Stacks")
tab_control.add(words_tab, text="Word Creator")


tab_control.pack(expand=1, fill="both")



root.mainloop()