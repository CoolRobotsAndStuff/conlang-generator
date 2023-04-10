import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from copy import deepcopy, copy

from gui.toggle_button import ToggleButton

class Searcher:
    def __init__(self, master, dict_to_search, selected_item_callback) -> None:
        self.dict_to_search = dict_to_search

        self.frame = ttk.Frame(master)

        self.searched_text = ttk.StringVar()
        self.searched_text.trace_add("write", self.search)
        self.search_box = ttk.Entry(self.frame, textvariable=self.searched_text)

        self.search_results_frame = ttk.Frame(self.frame)

        self.selected_item = ("", "")

        self.selected_item_callback = selected_item_callback

        self.result_buttons = []

    def delete_results(self):
        for item in self.search_results_frame.winfo_children():
            item.destroy()

    def untoggle_all(self):
        for button in self.result_buttons:
            button.untoggle()

    def get_select_item_function(self, item):
        def select_item():
            self.selected_item = item
            self.selected_item_callback(item)
            self.untoggle_all()
            print("set selected item to", item)
        return select_item


    def show_results(self, results):
        self.delete_results()
        self.result_buttons = []
        for result in results:
            item = (result, self.dict_to_search[result])
            result_button = ToggleButton(self.search_results_frame, result, command=self.get_select_item_function(item))
    
            result_button.pack(side=TOP, pady=5, fill=X, padx=10)

            if result == self.selected_item[0]:
                result_button.toggle()

            self.result_buttons.append(result_button)
            

    def search(self, *args):
        self.show_results(self.get_results())

    def get_results(self):
        results = {}
        for key in self.dict_to_search:
            if self.searched_text.get() in key:
                results[key] = self.dict_to_search[key]

        return results
    
    def pack(self):
        self.search_box.pack(fill=X, side=TOP, padx=10)
        self.search_results_frame.pack(fill=X, side=TOP)
        #self.frame.pack(fill=BOTH, side=LEFT, expand=True)
        self.search()




    