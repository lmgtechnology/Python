# keys

from datetime import datetime

def get_date():
    return datetime.now().strftime("%Y%m%d.%H%M%S")


choices = {
    "a": "Weekday as locale’s abbreviated name",
    "A": "Weekday as locale’s full name",
    'w': "Weekday as a decimal number, where @is Sunday and 6 is Saturday"
}