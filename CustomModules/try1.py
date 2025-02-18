
def main():
    import argparse
    from argparse import RawDescriptionHelpFormatter
    usage = """
    Usage: script.py [OPTIONS]
    
    Options:
      -h, --help      Show this help message and exit
      -v, --version   Show the version information and exit
      -f, --file      Specify the input file
      -o, --output    Specify the output file
    
    Example:
      script.py -f input.txt -o output.txt
    """
    
    choices = {
        "d": "Short date",
        "a": "Weekday as locale’s abbreviated name",
        "A": "Weekday as locale’s full name"
    }
    parser = argparse.ArgumentParser(
        description=f" \
            python %(prog)s -f <FORMAT> where <FORMAT> is: \n \
                {choices} \
            ", \
            formatter_class=RawDescriptionHelpFormatter \
    )
    # Works below
    # parser.add_argument('--format', type=chr, default='d') 
    parser.add_argument("choices", nargs="+", help="Choices:")
    args = parser.parse_args()
    # parser.print_help() # Worked
    for choice in args.choices:
        print (choice)

    """
    parser = argparse.ArgumentParser(description="Process script options.", epilog=usage, 
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-f", "--format", type=str, help=f"Specify <FORMAT> where format is {choices}")
    parser.add_argument("-o", "--output", type=str, help="Specify the output file")
    parser.add_argument("-v", "--version", action="version", version="Script version 1.0")
    
    args = parser.parse_args()
    
    print("Processed options:", vars(args))
    """

if __name__ == "__main__":
    main()