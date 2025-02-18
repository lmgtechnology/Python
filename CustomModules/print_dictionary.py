import argparse
import ast

# Manually populate dictionary
"""
dictionary = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
"""
dictionary = {
    "d": "Short date",
    "a": "Weekday as locale’s abbreviated name",
    "A": "Weekday as locale’s full name"
}

def custom_help_message():
    help_text = "\nUsage: python %(prog)s <FORMAT>, where <FORMAT> is:\n\n"
    help_text += "\n".join([f"{key}: {value}" for key, value in dictionary.items()])
    return help_text

def main():
    parser = argparse.ArgumentParser(description="Print key-value pairs of a dictionary on separate lines.",
                                     epilog=custom_help_message(),
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("dictionary", type=str, nargs="?", help="Dictionary to print in key-value pairs")
    args = parser.parse_args()
    
    if args.dictionary:
        try:
            parsed_dict = ast.literal_eval(args.dictionary)
            if isinstance(parsed_dict, dict):
                for key, value in parsed_dict.items():
                    print(f"{key}: {value}")
            else:
                print("Error: Input is not a dictionary.")
        except Exception as e:
            print(f"Error parsing dictionary: {e}")
    else:
        for key, value in dictionary.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()