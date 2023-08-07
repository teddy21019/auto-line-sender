from abc import ABC, abstractmethod, abstractproperty
from ast import arg

Coordinate = tuple[int, int]

class Clicker(ABC):

    def __init__(self, *args):
        return self

    @abstractmethod
    def calibrate(self, coordinate_info: dict[str, Coordinate]):
        """ Allows you to calibrate the position of crucial components on the screen"""
        ...
    @abstractproperty
    def required_coordinate(self):
        ...

    @abstractmethod
    def search(self, search_content: str):
        ...

    @abstractmethod
    def type(self, type_content: str):
        ...

    @abstractmethod
    def send(self):
        ...

class LineClicker(Clicker):
    pass

class SkypeClicker(Clicker):
    pass

class ShopeeClicker(Clicker):
    pass

class TestClicker(Clicker):

    def __init__(self, *args):
        print("Test clicker created")

    @property
    def required_coordinate(self):
        return ["search", "type", "send"]

    def calibrate(self, coordinate_info: dict[str, Coordinate]):

        try:
            self.search_box_pos = coordinate_info['search']
            self.type_box_pos = coordinate_info['type']
            self.send_box_pos = coordinate_info['send']
        except:
            raise KeyError(f"Current coordinate info does not match. Must include: {self.required_coordinate}")

        print(f"Search box is set at {self.search_box_pos}")
        print(f"Type box is set at {self.type_box_pos}")
        print(f"Send button is set at {self.send_box_pos}")

    def search(self, search_content: str):
        print(f"Click the search box at {self.search_box_pos}")
        print(f"Type in '{search_content}'")

    def type(self, type_content: str):
        print(f"Click the typing area at {self.type_box_pos}")
        print(f"Type {type_content}")

    def send(self):
        print(f"Click send button at {self.send_box_pos}")


class ClickerFactory:

    def __init__(self, coordinate_info: dict[str, dict[str, Coordinate]]|None = None):
        if coordinate_info is not None:
            self.coordinate_info = coordinate_info

    def create_clicker(self, messenger_type: str, *args) -> Clicker:

        c: Clicker
        if messenger_type == 'line':
            c = LineClicker(args)
            c.calibrate(self.coordinate_info['line'])

        elif messenger_type == 'skype':
            c = SkypeClicker(args)
            c.calibrate(self.coordinate_info['skype'])

        elif messenger_type == 'shopee':
            c = ShopeeClicker(args)
            c.calibrate(self.coordinate_info['shopee'])

        elif messenger_type == "test":
            c = TestClicker(args)
            c.calibrate(self.coordinate_info['test'])
        else:
            raise ValueError("Unknown type of messenger!!")
        return c