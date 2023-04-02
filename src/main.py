import tkinter as tk

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from searchable_dict import SearchableDict

root = ttk.Window(themename="darkly")

root.geometry("400x400")

root.title("Hello")

tab_control = ttk.Notebook(root)

stacks_tab = ttk.PanedWindow(tab_control) 


stacks_search = SearchableDict(stacks_tab)

stacks_tab.add(stacks_search.frame)

stacks_search.members["hello"] = 1
stacks_search.members["helloa"] = 2

stacks_search.pack()

words_tab =  ttk.Frame(tab_control)

tab_control.add(stacks_tab, text="Characteristic Stacks")
tab_control.add(words_tab, text="Word Creator")


tab_control.pack(expand=1, fill="both")

root.mainloop()