from .Clicker import Clicker
import pandas as pd

class Seller:

    def __init__(self, id:str , group_name:str , url:str , clicker: Clicker):
        self.id = id
        self.group_name = group_name
        self.url = url
        self.clicker = clicker

    def act(self):
        message = self.generate_message()

        self.clicker.search(self.group_name)
        self.clicker.type(message, at_all=True)

        ## wait for confirm

        self.clicker.send()

    def generate_message(self):
        return f"親愛的賣家您好，以下是連結：{self.url} 。請協助填寫，謝謝！"


def df_to_sellers(df:pd.DataFrame, clicker: Clicker, Seller_Class: type(Seller) = Seller):
    sellers_list = []
    for index, row in df.iterrows():
        _id = row['shopid']
        group_name = row['group_name']
        url = row['new_sheet']
        sellers_list.append(
            Seller_Class(_id, group_name, url, clicker)
        )
    return sellers_list