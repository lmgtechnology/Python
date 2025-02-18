import argparse

# Manually populate the dictionary
dictionary = {
    "d": "Short date",
    "a": "Weekday as locale’s abbreviated name",
    "A": "Weekday as locale’s full name"
}

def print_dict(d, format_key):
    """Print dictionary key-value pairs based on the specified format key."""
    found = False
    for key, value in d.items():
        if format_key == 'all' or format_key == key:
            print(f"{key}: {value}")
            found = True
    if not found:
        print(f"No entries found for format key: '{format_key}'")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description='Print elements of a dictionary based on key text.',
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # Add arguments
    parser.add_argument('--format', type=str, default='all',
                        help='Specify a key to filter the dictionary.\n'
                             'If "all", print all key-value pairs.\n'
                             'Example: --format d  (prints only the short date field)\n'
                             '         --format a  (prints only the abbreviated weekday field)')

    # Add help message with example dictionary
    parser.epilog = "Example Dictionary:\n" + '\n'.join(f"  {key}: {value}" for key, value in dictionary.items())

    # Parse arguments
    args = parser.parse_args()

    # Print dictionary based on the provided format
    print_dict(dictionary, args.format)

if __name__ == "__main__":
    main()