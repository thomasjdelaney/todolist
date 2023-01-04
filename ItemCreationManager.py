"""For creating a pop-up window that is used to create an Item for the ToDoList"""
import tkinter as tk


class ItemCreationManager:
    """Needs name and description fields."""
    def __init__(self):
        """For initialising the object."""
        self.top_level = None
        self.name_entry = None
        self.description_text = None
        self.set_top_level()
        self.set_name_entry()
        self.set_description_text()

    def set_top_level(self):
        """For setting up the window"""
        self.top_level = tk.Toplevel()
        self.top_level.title('Add item')
        self.top_level.geometry('300x300')
        self.top_level.resizable(True, True)
        self.top_level.config(bg='black')

    def set_name_entry(self):
        """For setting the name label and entry box."""
        tk.Label(self.top_level, text='name:', fg='White', bg='Black', font=('Ariel', 15), wraplength=300).pack()
        self.name_entry = tk.Entry(self.top_level)
        self.name_entry.pack(fill='x')

    def set_description_text(self):
        """For setting the description label and entry box."""
        tk.Label(self.top_level, text='description:', fg='White', bg='Black', font=('Ariel', 15), wraplength=300).pack()
        self.description_text = tk.Text(self.top_level)
        self.description_text.pack(fill=tk.BOTH)
