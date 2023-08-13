from .Clicker import Clicker
import pandas as pd
from .MessageTemplate import message_templates

class Seller:

    def __init__(self, id:str , group_name:str , url:str , clicker: Clicker):
        self.id = id
        self.group_name = group_name
        self.url = url
        self.next_month = None #
        self.clicker = clicker

    def act(self, message_type = 'default'):
        message = self.generate_message(message_type)

        self.clicker.search(self.group_name)
        self.clicker.type(message, at_all=True)

        ## wait for confirm

        self.clicker.send()

    def generate_message(self, message_type = 'default'):
        template = message_templates.get_template(message_type) or message_templates.get_template('default')
        return template.safe_substitute(group_name=self.group_name, url=self.url, id = self.id)


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