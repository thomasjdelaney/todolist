import tkinter as tk


class BlankFrame(tk.Frame):

    def __init__(self, parent, controller) -> None:
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # self.pack(expand=True, fill=tk.BOTH)
        tk.Label(self, text='Blank frame', fg='White', bg='Black', font=('Ariel', 15), wraplength=300).pack(
            fill=tk.BOTH)
