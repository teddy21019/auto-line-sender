from .Clicker import Clicker

class Seller:

    def __init__(self, id:str , group_name:str , url:str , clicker: Clicker):
        self.id = id
        self.group_name = group_name
        self.url = url
        self.clicker = clicker

    def act(self):
        message = self.generate_message()

        self.clicker.search(self.group_name)
        self.clicker.type(message)

        ## wait for confirm

        self.clicker.send()

    def generate_message(self):
        return f"親愛的賣家您好，以下是連結：{self.url} 。請協助填寫，謝謝！"