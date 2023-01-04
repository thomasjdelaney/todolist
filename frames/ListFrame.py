import tkinter as tk


class ListFrame(tk.Frame):
    """A class for containing the frame showing the label, and list frame."""
    def __init__(self, parent, controller) -> None:
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.pack(expand=True, fill='both', side=tk.LEFT)
        self.entry_box = None
        self.tasks = None
        self.set_tasks()
        self.set_entry_box()
        self.set_add_delete_buttons()

    def set_tasks(self) -> None:
        self.tasks = tk.Listbox(self, selectbackground='Gold', bg='Silver', font=('Helvetica', 12), height=12, width=25)
        scroller = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.tasks.yview)
        scroller.pack(side='right', fill='y')
        self.tasks.config(yscrollcommand=scroller.set)
        self.tasks.pack(expand=True, fill="both")

    def get_tasks(self) -> tk.Listbox:
        return self.tasks

    def set_entry_box(self) -> None:
        """Creating the Entry widget where the user can enter a new item"""
        self.entry_box = tk.Entry(self)
        self.entry_box.pack(fill='x')

    def get_entry_box(self) -> tk.Entry:
        return self.entry_box

    def set_add_delete_buttons(self) -> None:
        """For putting the add and delete buttons in a frame side by side."""
        add_button_frame = tk.Frame(self)
        add_button_frame.pack(expand=True, side=tk.LEFT, fill=tk.BOTH)
        delete_button_frame = tk.Frame(self)
        delete_button_frame.pack(expand=True, side=tk.RIGHT, fill=tk.BOTH)
        self.set_add_item_button(button_frame=add_button_frame)
        self.set_delete_item_button(button_frame=delete_button_frame)

    def set_add_item_button(self, button_frame: tk.Frame) -> None:
        tk.Button(
            button_frame, text='Add Item', bg='Azure', font=('Helvetica', 12),
            command=lambda: self.controller.show_frame('ItemCreationManager')).pack(fill='both')

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
