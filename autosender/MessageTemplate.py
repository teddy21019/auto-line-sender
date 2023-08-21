from pathlib import Path
import yaml
from string import Template
from datetime import datetime, timedelta
import calendar


class MessageTemplates:
    def __init__(self, template_file: str|Path):
        self.templates = self.load_templates(template_file)

    def load_templates(self, template_file:str|Path):
        with open(template_file, 'r', encoding='utf-8') as file:
            templates = yaml.safe_load(file)
        return templates
        
    def get_template(self, template_name) -> Template:
        template = Template(self.templates.get(template_name))
        template = Template(self.fill_datetime(template))

        return template

    def fill_datetime(self, template:Template):
        current_date = datetime.now()
        
        next_month = (current_date.replace(day=28) + timedelta(days=4)).month

        last_day_of_this_month = calendar.monthrange(current_date.year, current_date.month)[1]

        last_day_of_this_month = current_date.replace(day=last_day_of_this_month)

        return template.safe_substitute(
            year = current_date.year,
            month = current_date.month,
            next_month = next_month,
            last_day_of_this_month = last_day_of_this_month.strftime("%#m/%#d")
            )

def find_unfilled_fields(template):
    import re

    placeholders = re.findall(r'\{(.+?)\}', template)
    return placeholders

# Instantiate the MessageTemplates class with the template file path
message_templates = MessageTemplates("message-template/messages.yaml")
