# keys

import argparse
from datetime import datetime

def main():
    import argparse, locale, os

    parser = argparse.ArgumentParser()
    program_file = os.path.basename(__file__)

    args = parser.parse_args()

    version = "1.0"
    parser.add_argument('variable_length', type=int, help='Length of variable being passed')
    parser.add_argument('line_length', type=int, help='Total length of line, including variable and spaces')


choices = {
    "a": "Weekday as locale’s abbreviated name",
    "A": "Weekday as locale’s full name",
    'w': "Weekday as a decimal number, where @is Sunday and 6 is Saturday"
}