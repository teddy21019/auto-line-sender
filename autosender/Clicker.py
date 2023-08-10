from abc import ABC, abstractmethod, abstractproperty
import pyautogui as pt
import keyboard
import pyperclip
from time import sleep
from typing import Self

pt.FAILSAFE = True
pt.PAUSE = 1 

Coordinate = tuple[int, int]

class Clicker(ABC):

    def __init__(self, *args):
        return

    @abstractmethod
    def calibrate(self, coordinate_info: dict[str, Coordinate]) -> Self:
        """ Allows you to calibrate the position of crucial components on the screen"""
        ...
    @abstractproperty
    def required_coordinate(self):
        ...

    @abstractmethod
    def search(self, search_content: str):
        ...

    @abstractmethod
    def type(self, type_content: str, at_all:bool = False):
        ...

    @abstractmethod
    def send(self):
        ...

    @abstractmethod
    def check(self):
        ...


class LineClicker(Clicker):

    def __init__(self, *args):
        return

    def calibrate(self, coordinate_info: dict[str, Coordinate]) -> Self:
        """ Allows you to calibrate the position of crucial components on the screen"""
        try:
            self.search_box_pos = coordinate_info['search']
            self.first_result_pos = coordinate_info['first_result']
            self.type_box_pos = coordinate_info['type']
        except:
            raise KeyError(f"Current coordinate info does not match. Must include: {self.required_coordinate}")
        finally:
            return self
    @property
    def required_coordinate(self):
        return ["search", "first_result", "type"]

    def search(self, search_content: str):
        #click search box
        pt.click(*self.search_box_pos)  # star: decompose tuple into separate parameters
        delete_texts()
        type_in(search_content)
        sleep(1)
        pt.click(*self.first_result_pos)

    def type(self, type_content: str, at_all: bool = False):
        pt.click(*self.type_box_pos)
        if at_all:
            type_in("@")
            pt.press('enter')
        type_in(type_content)

    def send(self):
        while True:
            if keyboard.is_pressed('enter'):
                break

    def check(self):
        series_of_positions = [
            self.search_box_pos,
            self.first_result_pos,
            self.type_box_pos
        ]

        for position in series_of_positions:
            pt.moveTo(*position)
            pt.press("ctrl")
            sleep(1)    
        return

class SkypeClicker(Clicker):

    def __init__(self, *args):
        return

    def calibrate(self, coordinate_info: dict[str, Coordinate]) -> Self:
        """ Allows you to calibrate the position of crucial components on the screen"""
        try:
            self.search_box_pos = coordinate_info['search']
            self.first_result_pos = coordinate_info['first_result']
            self.type_box_pos = coordinate_info['type']
        except:
            raise KeyError(f"Current coordinate info does not match. Must include: {self.required_coordinate}")
        finally:
            return self
    @property
    def required_coordinate(self):
        return ["search", "first_result", "type"]

    def search(self, search_content: str):
        #click search box
        pt.click(*self.search_box_pos)  # star: decompose tuple into separate parameters
        delete_texts()
        type_in(search_content)
        sleep(1)
        pt.click(*self.first_result_pos)

    def type(self, type_content: str, at_all: bool = False):
        pt.click(*self.type_box_pos)
        if at_all:
            type_in("@")
            pt.press('tab')
        type_in(type_content)

    def send(self):
        while True:
            if keyboard.is_pressed('enter'):
                break

    def check(self):
        series_of_positions = [
            self.search_box_pos,
            self.first_result_pos,
            self.type_box_pos
        ]

        for position in series_of_positions:
            pt.moveTo(*position)
            pt.press("ctrl")
            sleep(1)    
        return


class ShopeeClicker(Clicker):
    pass

    def calibrate(self, coordinate_info: dict[str, Coordinate]):
        """ Allows you to calibrate the position of crucial components on the screen"""
        ...
    @property
    def required_coordinate(self):
        return ""

    def search(self, search_content: str):
        return

    def type(self, type_content: str):
        return

    def send(self):
        return

class TestClicker(Clicker):

    def __init__(self, *args):
        print("Test clicker created")

    @property
    def required_coordinate(self):
        return ["search", "type", "send"]

    def calibrate(self, coordinate_info: dict[str, Coordinate]) -> Self:

        try:
            self.search_box_pos = coordinate_info['search']
            self.type_box_pos = coordinate_info['type']
            self.send_box_pos = coordinate_info['send']
        except:
            raise KeyError(f"Current coordinate info does not match. Must include: {self.required_coordinate}")

        print(f"Search box is set at {self.search_box_pos}")
        print(f"Type box is set at {self.type_box_pos}")
        print(f"Send button is set at {self.send_box_pos}")
        return self

    def search(self, search_content: str):
        print(f"Click the search box at {self.search_box_pos}")
        print(f"Type in '{search_content}'")
        print(f"Click the first result")

    def type(self, type_content: str):
        print(f"Click the typing area at {self.type_box_pos}")
        print("Type: @"); print("press enter")
        print(f"Type {type_content}")

    def send(self):
        print(f"Click send button at {self.send_box_pos}")

    def check(self):
        return

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
    

def type_in(content: str):
    pyperclip.copy(content)
    pt.hotkey("ctrl", "v")
    return

def delete_texts():
    pt.hotkey("ctrl", "a")
    pt.press("delete")
    
def wait_for_start():
    keyboard.wait("f12")