"""For creating a pop-up window that is used to create an Item for the ToDoList"""
import tkinter as tk


class ItemCreationManager(tk.Frame):
    """Needs name and description fields."""
    def __init__(self, parent, controller):
        """For initialising the object."""
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # self.pack(expand=True, fill=tk.BOTH)
        tk.Label(self, text='Add item', fg='White', bg='Black', font=('Ariel', 15), wraplength=300).pack(
            fill=tk.BOTH)
        self.name_entry = None
        self.description_text = None
        self.set_name_entry()
        self.set_description_text()

    def set_name_entry(self):
        """For setting the name label and entry box."""
        tk.Label(self, text='name:', fg='White', bg='Black', font=('Ariel', 15), wraplength=300).pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(fill='x')

    def set_description_text(self):
        """For setting the description label and entry box."""
        tk.Label(self, text='description:', fg='White', bg='Black', font=('Ariel', 15), wraplength=300).pack()
        self.description_text = tk.Text(self)
        self.description_text.pack(fill=tk.BOTH)
