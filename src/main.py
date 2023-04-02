import tkinter as tk

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from searcher import Searcher

# Root
root = ttk.Window(themename="darkly")
root.geometry("400x400")
root.title("Conlang creator")

# Tabs
tab_control = ttk.Notebook(root)

#Stacks
stacks_tab = ttk.PanedWindow(tab_control, orient=HORIZONTAL)

my_dict = {
    "verb":"verb_config",
    "noun":"noun_config",
    "adverb":"adverb_config"
}

stack_modifier_frame = ttk.Frame(stacks_tab)

current_stack_name = ttk.StringVar()
current_stack_name_label = ttk.Label(stack_modifier_frame, textvariable=current_stack_name)

current_stack_name_label.pack()

def show_searched_characteristic(item):
    current_stack_name.set(item[0])

stack_searcher = Searcher(stacks_tab, my_dict, show_searched_characteristic)

stacks_tab.add(stack_searcher.frame)
stacks_tab.add(stack_modifier_frame)

stacks_tab.pack()

stack_searcher.pack()
#stack_modifier_frame.pack(fill=BOTH)




words_tab =  ttk.Frame(tab_control)

tab_control.add(stacks_tab, text="Characteristic Stacks")
tab_control.add(words_tab, text="Word Creator")


tab_control.pack(expand=1, fill="both")



root.mainloop()