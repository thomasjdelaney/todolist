"""A class for a to-do list manager"""
import tkinter as tk
from ItemCreationManager import ItemCreationManager


class ToDoListManager:
    """For managing the whole To-do list manager"""
    def __init__(self) -> None:
        """For initialising the object."""
        self.entry_box = None
        self.tasks = None
        self.root = tk.Tk()
        self.set_root()
        self.set_header()
        self.set_task_list_box()
        self.set_entry_box()
        self.set_add_delete_buttons()

    def set_root(self) -> None:
        """For making the root window settings"""
        self.root.title('To-do list')
        self.root.geometry('300x400')
        self.root.resizable(True, True)
        self.root.config(bg='Black')
        self.root.bind('<Return>', self.add_item_event)

    def set_header(self) -> None:
        """For setting the header in the root window"""
        tk.Label(
            self.root, text='Python to-do list', fg='White', bg='Black', font=('Ariel', 15),
            wraplength=300).pack()

    def set_task_list_box(self) -> None:
        """For setting up the list box where the tasks are stored."""
        task_frame = tk.Frame(self.root)
        task_frame.pack(expand=True, fill='both')
        self.tasks = tk.Listbox(
            task_frame, selectbackground='Gold', bg='Silver', font=('Helvetica', 12), height=12, width=25)
        scroller = tk.Scrollbar(task_frame, orient=tk.VERTICAL, command=self.tasks.yview)
        scroller.pack(side='right', fill='y')
        self.tasks.config(yscrollcommand=scroller.set)
        self.tasks.pack(expand=1, fill="both", side="left")
        self.add_existing_items()

    def add_existing_items(self) -> None:
        """Adding items to the Listbox that are already in the tasks.txt file"""
        with open('tasks.txt', 'r+') as tasks_list:
            for task in tasks_list:
                self.tasks.insert(tk.END, task)
            tasks_list.close()

    def set_entry_box(self) -> None:
        """Creating the Entry widget where the user can enter a new item"""
        self.entry_box = tk.Entry(self.root)
        self.entry_box.pack(fill='x')

    def set_add_delete_buttons(self) -> None:
        """For putting the add and delete buttons in a frame side by side."""
        add_button_frame = tk.Frame(self.root)
        add_button_frame.pack(expand=True, side=tk.LEFT, fill=tk.BOTH)
        delete_button_frame = tk.Frame(self.root)
        delete_button_frame.pack(expand=True, side=tk.RIGHT, fill=tk.BOTH)
        self.set_add_item_button(button_frame=add_button_frame)
        self.set_delete_item_button(button_frame=delete_button_frame)

    def set_add_item_button(self, button_frame: tk.Frame) -> None:
        tk.Button(
            button_frame, text='Add Item', bg='Azure', font=('Helvetica', 12),
            command=lambda: ItemCreationManager()).pack(fill='both')

    def set_delete_item_button(self, button_frame: tk.Frame) -> None:
        tk.Button(
            button_frame, text='Delete Item', bg='Azure', font=('Helvetica', 12),
            command=lambda: self.delete_item()).pack(fill='both')

    def add_item(self, entry: tk.Entry) -> None:
        new_task = entry.get()
        if new_task:
            self.tasks.insert(tk.END, new_task)
            with open('tasks.txt', 'a') as tasks_list_file:
                tasks_list_file.write(f'{new_task}\n')
            entry.delete(0, tk.END)

    def add_item_event(self, event: tk.Event):
        """For binding to the <Return> button"""
        self.add_item(self.entry_box)

    def delete_item(self) -> None:
        """For deleting the active item from the Listbox and the file. If there is no '\n' at the end of the
        active_item, then add one, I suppose."""
        active_item = self.tasks.get(tk.ACTIVE)
        active_item = f'{active_item}\n' if not active_item.endswith('\n') else active_item
        self.tasks.delete(tk.ACTIVE)
        with open('tasks.txt', 'r') as tasks_list_file:
            lines = tasks_list_file.readlines()
        if active_item in lines:
            lines.remove(active_item)
        else:
            print(f'{active_item} not in lines!')
            print(lines)
        with open('tasks.txt', 'w') as tasks_list_file:
            tasks_list_file.writelines(lines)
