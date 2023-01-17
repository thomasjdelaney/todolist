"""A class for a to-do list manager"""
import tkinter as tk
from frames.ListFrame import ListFrame
from frames.BlankFrame import BlankFrame
from frames.ItemCreationManager import ItemCreationManager


class ToDoListManager:
    """For managing the whole To-do list manager"""
    def __init__(self) -> None:
        """For initialising the object."""
        self.entry_box = None
        self.tasks = None
        self.left_frame = None
        self.right_frame = None
        self.list_frame = None
        self.blank_frame = None
        self.root = tk.Tk()
        self.set_root()
        self.set_header()
        self.set_task_list_box()
        self.set_blank_frame()

    def set_left_right_frames(self):
        self.left_frame = tk.Frame(self.root)
        self.left_frame.pack(expand=True, fill='both', side=tk.LEFT)
        self.right_frame = tk.Frame(self.root)
        self.right_frame.pack(expand=True, fill='both', side=tk.RIGHT)
        self.right_frame.grid_rowconfigure(0, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)
        self.root.frames = {}
        for fr in [BlankFrame, ItemCreationManager]:
            page_name = fr.__name__
            frame = fr(parent=self.right_frame, controller=self)
            self.root.frames[page_name] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame('BlankFrame')

    def show_frame(self, page_name) -> None:
        """For showing the frame with the given name"""
        frame = self.root.frames.get(page_name)
        frame.tkraise()

    def set_root(self) -> None:
        """For making the root window settings"""
        self.root.title('To-do list')
        self.root.geometry('700x400')
        self.root.resizable(True, True)
        self.root.config(bg='Black')
        self.root.bind('<Return>', self.add_item_event)
        self.set_left_right_frames()

    def set_header(self) -> None:
        """For setting the header in the root window"""
        tk.Label(
            self.left_frame, text='Python to-do list', fg='White', bg='Black', font=('Ariel', 15),
            wraplength=300).pack(fill=tk.BOTH)

    def set_task_list_box(self) -> None:
        """For setting up the list box where the tasks are stored."""
        self.list_frame = ListFrame(self.left_frame, controller=self)
        self.tasks = self.list_frame.tasks
        self.entry_box = self.list_frame.entry_box
        self.add_existing_items()

    def set_blank_frame(self) -> None:
        """For setting up the blank frame on the right hand side"""
        self.blank_frame = BlankFrame(self.right_frame, controller=self)

    def add_existing_items(self) -> None:
        """Adding items to the Listbox that are already in the tasks.txt file"""
        with open('tasks.txt', 'r+') as tasks_list:
            for task in tasks_list:
                self.tasks.insert(tk.END, task)
            tasks_list.close()

    def add_item_event(self, event: tk.Event) -> None:
        """For binding to the <Return> button"""
        self.list_frame.add_item(self.entry_box)

    def add_item(self) -> None:
        """For reading in the info from name and description on ItemCreationManager, adding it to the items dict and
        saving that down"""
        name = self.root.frames['ItemCreationManager'].name_entry.get()
        desc = self.root.frames['ItemCreationManager'].description_text.get('1.0', 'end-1c')
        return None