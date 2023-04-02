import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class SearchableDict:
    def __init__(self, master) -> None:
        self.members = {}

        self.frame = ttk.Frame(master)

        self.searched_text = ttk.StringVar()
        self.searched_text.trace_add("write", self.search)
        self.search_box = ttk.Entry(self.frame, textvariable=self.searched_text)

        self.search_results_frame = ttk.Frame(self.frame)

    def delete_results(self):
        for item in self.search_results_frame.winfo_children():
            item.destroy()

    def show_results(self, results):
        self.delete_results()
        for result in results:
            result_button = ttk.Button(self.search_results_frame, text=result)
            result_button.pack(side=BOTTOM, pady=5, fill=X)

    def search(self, *args):
        self.show_results(self.get_results())

    def get_results(self):
        results = {}
        for key in self.members:
            if self.searched_text.get() in key:
                results[key] = self.members[key]

        return results
    
    def pack(self):
        self.search_box.pack(fill=X, side=TOP)
        self.search_results_frame.pack(fill=X, side=BOTTOM)
        self.frame.pack(fill=X)
        self.search()




    