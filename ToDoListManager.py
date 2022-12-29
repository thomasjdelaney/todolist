"""A class for a to-do list manager"""
import tkinter as tk


def add_item(entry: tk.Entry, listbox: tk.Listbox):
    new_task = entry.get()
    listbox.insert(tk.END, new_task)
    with open('tasks.txt', 'a') as tasks_list_file:
        tasks_list_file.write(f'\n{new_task}')


def delete_item(listbox: tk.Listbox):
    listbox.delete(tk.ACTIVE)
    with open('tasks.txt', 'r+') as tasks_list_file:
        lines = tasks_list_file.readlines()
        tasks_list_file.truncate()
        for line in lines:
            if listbox.get(tk.ACTIVE) == line[:-2]:
                lines.remove(line)
            tasks_list_file.write(line)
        tasks_list_file.close()


class ToDoListManager:
    """For managing the whole To-do list manager"""
    def __init__(self) -> None:
        """For initialising the object."""
        self.entry_box = None
        self.tasks = None
        self.root = tk.Tk()
        self.set_root()
        self.set_header()

    def set_root(self) -> None:
        """For making the root window settings"""
        self.root.title('To-do list')
        self.root.geometry('300x400')
        self.root.resizable(True, True)
        self.root.config(bg='Grey')

    def set_header(self) -> None:
        """For setting the header in the root window"""
        tk.Label(self.root, text='Python to-do list', bg='Grey', font=('Ariel', 15), wraplength=300).place(x=35, y=0)

    def set_task_list_box(self) -> None:
        """For setting up the list box where the tasks are stored."""
        self.tasks = tk.Listbox(
            self.root, selectbackground='Gold', bg='Silver', font=('Helvetica', 12), height=12, width=25)
        scroller = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.tasks.yview)
        scroller.place(x=260, y=50, height=232)
        self.tasks.config(yscrollcommand=scroller.set)
        self.tasks.place(x=35, y=50)

    def add_existing_items(self) -> None:
        """Adding items to the Listbox that are already in the tasks.txt file"""
        with open('tasks.txt', 'r+') as tasks_list:
            for task in tasks_list:
                self.tasks.insert(tk.END, task)
            tasks_list.close()

    def set_entry_box(self) -> None:
        """Creating the Entry widget where the user can enter a new item"""
        self.entry_box = tk.Entry(self.root, width=37)
        self.entry_box.place(x=35, y=310)

    def set_add_item_button(self) -> None:
        tk.Button(
            self.root, text='Add Item', bg='Azure', width=10, font=('Helvetica', 12),
            command=lambda: add_item(self.entry_box, self.tasks)).place(x=45, y=350)

    def set_delete_item_button(self) -> None:
        tk.Button(
            self.root, text='Delete Item', bg='Azure', width=10, font=('Helvetica', 12),
            command=lambda: delete_item(self.tasks)).place(x=150, y=350)
