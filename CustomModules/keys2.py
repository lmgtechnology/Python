import argparse, textwrap

# choices = ["f", "d", "D"]
debug = True

choices = {
    "d": "Short date",
    "a": "Weekday as locale’s abbreviated name",
    "A": "Weekday as locale’s full name"
}

parser = argparse.ArgumentParser(
    description=f" \
        python %(prog)s --format <FORMAT>, \n \
            where <FORMAT> choices are: \n \
            {choices} \
        "
)
parser.add_argument('--format', type=chr, default='d') \
    parser.print_help()