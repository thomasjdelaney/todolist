"""A class for defining ToDoList Items"""
import uuid


class Item:
    """Attributes:
        id:
        name:
        description:
    Functions:
        get_methods: for id, name, description"""
    def __init__(self, name: str, description: str) -> None:
        """For initialising the object.
        Args:
            name: the name of the list item
            description: a short description of the item"""
        self.id: str = uuid.uuid4().hex
        self.name: str = name
        self.description: str = description

    def get_id(self) -> str:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description
