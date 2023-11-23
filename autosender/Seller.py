from abc import ABC, abstractmethod, abstractproperty
from .Clicker import Clicker
import pandas as pd
from .MessageTemplate import message_templates

class Seller(ABC):

    def __init__(self, id:str , group_name:str, PIC_name:str, url:str , clicker: Clicker):
        self.id         = id
        self.group_name = group_name
        self.PIC_name   = PIC_name # Test
        self.url        = url
        self.next_month = None #
        self.clicker    = clicker

    @abstractmethod
    def act(self, message_type = 'default'):
        ...

    @abstractmethod
    def generate_message(self, message_type = 'default'):
        ...

class Ordinary_Seller(Seller):

    def __init__(self, id:str , group_name:str, PIC_name:str, url:str , clicker: Clicker):
        self.id         = id
        self.group_name = group_name
        self.PIC_name   = PIC_name # Test
        self.url        = url
        self.next_month = None #
        self.clicker    = clicker

    def act(self, message_type = 'default'):
        message = self.generate_message(message_type)

        self.clicker.search(self.group_name)
        # self.clicker.type(message, at_all=True)
        self.clicker.type(self.PIC_name, message, at_all=True) # Test

        ## wait for confirm

        self.clicker.send()

    def generate_message(self, message_type = 'default'):
        template = message_templates.get_template(message_type) or message_templates.get_template('default')
        return template.safe_substitute(group_name=self.group_name, url=self.url, id = self.id)

class Seller_with_picture(Seller):

    def __init__(self, id:str , group_name:str, PIC_name:str, url:str , clicker: Clicker):
        self.id         = id
        self.group_name = group_name
        self.PIC_name   = PIC_name # Test
        self.url        = url
        self.next_month = None #
        self.clicker    = clicker

    def act(self, message_type = 'default'):
        message = self.generate_message(message_type)

        self.clicker.search(self.group_name)
        # self.clicker.type(message, at_all=True)
        self.clicker.type(self.PIC_name, message, at_all=True) # Test

        self.clicker.send_file()

        ## wait for confirm

        self.clicker.send()

    def generate_message(self, message_type = 'default'):
        template = message_templates.get_template(message_type) or message_templates.get_template('default')
        return template.safe_substitute(group_name=self.group_name, url=self.url, id = self.id)
    
class Seller_search_content(Seller):

    def __init__(self, id:str , group_name:str, PIC_name:str, url:str , clicker: Clicker):
        self.id         = id
        self.group_name = group_name
        self.PIC_name   = PIC_name # Test
        self.url        = url
        self.next_month = None #
        self.clicker    = clicker

    def act(self, message_type = 'default'):
        message = self.generate_message(message_type)

        self.clicker.search(self.group_name)
        self.clicker.search_message()
        self.clicker.type(self.PIC_name, message, at_all=True) # Test

        ## wait for confirm
        self.clicker.send()

    def generate_message(self, message_type = 'default'):
        template = message_templates.get_template(message_type) or message_templates.get_template('default')
        return template.safe_substitute(group_name=self.group_name, url=self.url, id = self.id)
    
class Seller_disable_voucher(Seller):

    def __init__(self, promo_id: int, username: str, clicker: Clicker):
        self.promo_id   = promo_id
        self.username   = username
        self.next_month = None #
        self.clicker    = clicker

    def act(self):

        self.clicker.search(self.promo_id)

        self.clicker.disable()   


# def df_to_sellers(df:pd.DataFrame, clicker: Clicker, Seller_Class: type(Seller) = Seller):
def df_to_sellers(df:pd.DataFrame, clicker: Clicker, Seller_Class: type(Seller)):
    sellers_list = []
    for index, row in df.iterrows():
        _id        = row['shopid']
        group_name = row['group_name']
        PIC_name   = row['PIC']
        url        = row['url']
        sellers_list.append(
            Seller_Class(_id, group_name, PIC_name, url, clicker)
        )
    return sellers_list

def df_to_sellers_voucher(df:pd.DataFrame, clicker: Clicker, Seller_Class: type(Seller)):
    sellers_list = []
    for index, row in df.iterrows():
        promo_id = row['promotionid']
        username = row['tw username']
        sellers_list.append(
            Seller_Class(promo_id, username, clicker)
        )
    return sellers_list