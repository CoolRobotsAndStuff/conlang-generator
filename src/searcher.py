import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from copy import deepcopy, copy

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

        self.button_normal_colour = "#375a7f"
        self.button_pressed_colour = "#2c4866"

    def delete_results(self):
        for item in self.search_results_frame.winfo_children():
            item.destroy()
    
    def toggle(self, button: tk.Button):
        button.config(background=self.button_pressed_colour, relief="sunken")

    def untogle_all(self):
        for button in self.result_buttons:
            button.config(background=self.button_normal_colour, relief="flat")

    def get_select_item_function(self, item, button):
        def select_item():
            self.selected_item = item
            self.selected_item_callback(item)
            self.untogle_all()
            self.toggle(button)
            print("set selected item to", item)

        return select_item
    
    def get_color_changing_function(self, button, color):
        def change_color(e):
            button.config(background=color)

        return change_color


    def show_results(self, results):
        self.delete_results()
        self.result_buttons = []
        for result in results:
            item = (result, self.dict_to_search[result])
            result_button = copy(tk.Button(self.search_results_frame, 
                                           text=result))
            result_button.config(background=self.button_normal_colour, 
                                 activebackground=self.button_pressed_colour, 
                                 activeforeground="white",
                                 highlightbackground="#375a7f", 
                                 command=self.get_select_item_function(item, result_button))
            #result_button.bind('<Enter>', self.get_color_changing_function(result_button, "grey"))
            #result_button.bind('<Leave>', self.get_color_changing_function(result_button, self.off_colour))
            result_button.pack(side=TOP, pady=5, fill=X)

            if result == self.selected_item[0]:
                self.toggle(result_button)

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
        self.search_box.pack(fill=X, side=TOP)
        self.search_results_frame.pack(fill=X, side=TOP)
        #self.frame.pack(fill=BOTH, side=LEFT, expand=True)
        self.search()




    