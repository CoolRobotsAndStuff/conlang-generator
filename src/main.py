import tkinter as tk

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from searcher import Searcher
from stack_editor import StackEditor

from characteristic import ComplexCharacteristic, Characteristic, CharacteristicStack
from characteristics.sufix import Sufix



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
gender.add_variant("femenino", Sufix("a"))
gender.add_variant("masculino", Sufix("o"))

number = ComplexCharacteristic("singular")
number.add_variant("singular", Characteristic())
number.add_variant("plural", Sufix("s"))

my_stacks["noun"].insert_item(1, "gender", gender)
my_stacks["noun"].insert_item(1, "number", number)


stack_editor = StackEditor(stacks_tab)


def show_searched_characteristic(item):
    stack_editor.set_stack(item[0], item[1])

stack_searcher = Searcher(stacks_tab, my_stacks, show_searched_characteristic)

stacks_tab.add(stack_searcher.frame)
stacks_tab.add(stack_editor.frame)

stacks_tab.pack()

stack_searcher.pack()
stack_editor.pack()




words_tab =  ttk.Frame(tab_control)

tab_control.add(stacks_tab, text="Characteristic Stacks")
tab_control.add(words_tab, text="Word Creator")


tab_control.pack(expand=1, fill="both")



root.mainloop()