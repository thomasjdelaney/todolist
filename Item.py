"""A class for defining ToDoList Items"""
import json


class Item:
    """Attributes:
        name:
        description:
    Functions:
        get_methods: for name, description"""
    def __init__(self, name: str, description: str) -> None:
        """For initialising the object.
        Args:
            name: the name of the list item
            description: a short description of the item"""
        self.name: str = name
        self.description: str = description

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    @staticmethod
    def load_by_name(name: str) -> 'Item':
        item = Item('', '')
        with open('tasks.json', 'r') as f:
            tasks_dict = json.load(f)
        for task_name, desc in tasks_dict.items():
            if name == task_name:
                item = Item(name=task_name, description=desc)
        return item

    def __repr__(self) -> str:
        return f'<Item: {self.name}: {self.description}>'
