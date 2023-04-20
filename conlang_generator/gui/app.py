import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from gui.searcher import Searcher
from gui.stack_editor import StackEditor
from gui.characteristic_editor import CharacteristicEditor


class App(ttk.Window):
    def __init__(self):
        super().__init__(themename='darkly')
        self.geometry("400x400")
        self.title("Conlang creator")

        self.tabs_control = ttk.Notebook(self)

        self.stacks_tab = ttk.PanedWindow(self.tabs_control, orient=HORIZONTAL)

        