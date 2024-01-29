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
    def search_message(self):
        ...

    @abstractmethod
    def type(self, type_content: str, at_all:bool = False):
        ...

    @abstractmethod
    def disable(self):
        ...

    @abstractmethod
    def send_file(self):
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
        print(search_content)
        type_in(search_content)
        sleep(1)
        pt.click(*self.first_result_pos)

    def search_message(self):
        ...

    def type(self, PIC_name: str, type_content: str, at_all: bool = False):
        pt.click(*self.type_box_pos)
        if at_all:
            type_in("@")
            type_in(PIC_name) # Test
            pt.press('tab')
        type_in(type_content)

    def disable(self):
        ...


    def send_file(self):
        ...

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

    def search_message(self):
        ...

    def type(self, PIC_name: str, type_content: str, at_all: bool = False):
        pt.click(*self.type_box_pos)
        if at_all:
            type_in("@")
            type_in(PIC_name)
            pt.press('tab')
        type_in(type_content)

    def disable(self):
        ...

    def send_file(self):
        ...

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

class Clicker_with_image(Clicker):

    def __init__(self, *args):
        return

    def calibrate(self, coordinate_info: dict[str, Coordinate]) -> Self:
        """ Allows you to calibrate the position of crucial components on the screen"""
        try:
            self.search_box_pos     = coordinate_info['search']
            self.first_result_pos   = coordinate_info['first_result']
            self.type_box_pos       = coordinate_info['type']
            self.add_file           = coordinate_info['add_file']
            self.file_1               = coordinate_info['file_1']
            # self.file_2               = coordinate_info['file_2']
            self.open_file          = coordinate_info['open_file']
        except:
            raise KeyError(f"Current coordinate info does not match. Must include: {self.required_coordinate}")
        finally:
            return self
    @property
    def required_coordinate(self):
        return ["search", "first_result", "type", "add_file", "file_1", "file_2", "open_file"]

    def search(self, search_content: str):
        #click search box
        pt.click(*self.search_box_pos)  # star: decompose tuple into separate parameters
        delete_texts()
        print(search_content)
        type_in(search_content)
        sleep(1)
        pt.click(*self.first_result_pos)

    def search_message(self):
        ...

    def type(self, PIC_name: str, type_content: str, at_all: bool = False):
        pt.click(*self.type_box_pos)
        if at_all:
            type_in("@")
            type_in(PIC_name) # Test
            pt.press('tab')
        type_in(type_content)

    def disable(self):
        ...

    def send_file(self):
        pt.click(*self.add_file)
        pt.click(*self.file_1)
        pt.click(*self.open_file)
        # sleep(1)
        # pt.click(*self.add_file)
        # # pt.click(*self.file_2)
        # pt.click(*self.open_file)
        

    def send(self):
        while True:
            if keyboard.is_pressed('enter'):
                break

    def check(self):
        series_of_positions = [
            self.search_box_pos,
            self.first_result_pos,
            self.type_box_pos,
            self.add_file,
            self.file_1,
            self.file_2,
            self.open_file
        ]

        for position in series_of_positions:
            pt.moveTo(*position)
            pt.press("ctrl")
            sleep(1)    
        return
    
class Clicker_find_message(Clicker):

    def __init__(self, *args):
        return

    def calibrate(self, coordinate_info: dict[str, Coordinate]) -> Self:
        """ Allows you to calibrate the position of crucial components on the screen"""
        try:
            self.search_box_pos = coordinate_info['search']
            self.first_result_pos = coordinate_info['first_result']
            self.search_message_pos = coordinate_info['message_search']
            self.search_message_box_pos = coordinate_info['type-in']
            self.search_type_pos = coordinate_info['search_type']
            self.message_pos = coordinate_info['pos_click']
            self.message_reply_pos = coordinate_info['reply']
            self.type_box_pos = coordinate_info['type']
        except:
            raise KeyError(f"Current coordinate info does not match. Must include: {self.required_coordinate}")
        finally:
            return self
    @property
    def required_coordinate(self):
        return ["search", "first_result", "type", "message_search", "type-in", "search_type", "pos_click", "reply"]

    def search(self, search_content: str):
        #click search box
        pt.click(*self.search_box_pos)  # star: decompose tuple into separate parameters
        delete_texts()
        print(search_content)
        type_in(search_content)
        sleep(1)
        pt.click(*self.first_result_pos)
    
    def search_message(self):
        pt.click(*self.search_message_pos)
        pt.click(*self.search_message_box_pos)
        type_in('全月補貼活動')
        sleep(1)
        pt.click(*self.search_type_pos)
        # pt.moveTo(*self.message_pos)
        pt.click(*self.message_pos, button='right')
        pt.click(*self.message_reply_pos)

    def type(self, PIC_name: str, type_content: str, at_all: bool = False):
        pt.click(*self.type_box_pos)
        if at_all:
            type_in("@")
            type_in(PIC_name) # Test
            pt.press('tab')
        type_in(type_content)

    def disable(self):
        ...

    def send_file(self):
        ...

    def send(self):
        while True:
            if keyboard.is_pressed('enter'):
                break

    def check(self):
        series_of_positions = [
            self.search_box_pos,
            self.first_result_pos,
            self.search_message_pos,
            self.search_message_box_pos,
            self.search_type_pos,
            self.message_pos,
            self.message_reply_pos,
            self.type_box_pos
        ]

        for position in series_of_positions:
            pt.moveTo(*position)
            pt.press("ctrl")
            sleep(1)    
        return

class Clicker_disable_voucher(Clicker):

    def __init__(self, *args):
        return

    def calibrate(self, coordinate_info: dict[str, Coordinate]) -> Self:
        """ Allows you to calibrate the position of crucial components on the screen"""
        try:
            self.search_box_pos         = coordinate_info['search']
            self.first_result_pos       = coordinate_info['first_result']
            self.type_box_pos           = coordinate_info['type']
            self.search_button          = coordinate_info['search_button']
            self.view_button            = coordinate_info['view_button']
            self.disable_button         = coordinate_info['disable_button']
            self.disable_comfirm_button = coordinate_info['disable_comfirm_button']
            self.return_button          = coordinate_info['return_button']
        except:
            raise KeyError(f"Current coordinate info does not match. Must include: {self.required_coordinate}")
        finally:
            return self
    @property
    def required_coordinate(self):
        return ["search", "first_result", "type", "search_button", "view_button", \
                "disable_button", "disable_comfirm_button", "return_button"]

    def search(self, search_content: str):
        #click search box
        pt.click(*self.search_box_pos)  # star: decompose tuple into separate parameters
        # delete_texts()
        print(search_content)
        type_in(search_content)
        sleep(1)
        pt.click(*self.search_button)
        sleep(1)
        pt.click(*self.view_button)
        sleep(1)

    def search_message(self):
        ...

    def type(self, PIC_name: str, type_content: str, at_all: bool = False):
        pt.click(*self.type_box_pos)
        if at_all:
            type_in("@")
            type_in(PIC_name) # Test
            pt.press('tab')
        type_in(type_content)

    def disable(self):
        pt.click(*self.disable_button)
        pt.click(*self.disable_comfirm_button)
        sleep(1)
        pt.click(*self.return_button)
        sleep(2)

    def send_file(self):
        ...
        
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

class AnnieClicker(Clicker):

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
        print(search_content)
        type_in(search_content)
        sleep(1)
        pt.click(*self.first_result_pos)

    def search_message(self):
        ...

    def type(self, type_content: str):
        pt.click(*self.type_box_pos)
        # if at_all:
        #     type_in("@")
        #     type_in(PIC_name) # Test
        #     pt.press('tab')
        type_in(type_content)

    def disable(self):
        ...


    def send_file(self):
        ...

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

    def search_message(self):
        ...

    def type(self, type_content: str, at_all:bool):
        print(f"Click the typing area at {self.type_box_pos}")
        if at_all:
            print("Type: @"); print("press tab")
        print(f"Type {type_content}")

    def disable(self):
        ...

    def send_file(self):
        ...

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
            c = Clicker_with_image(args)
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
    keyboard.wait("f9")