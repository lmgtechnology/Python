def right_justify(variable_length, line_length):
    import argparse, locale, os

    parser = argparse.ArgumentParser()
    program_file = os.path.basename(__file__)

    args = parser.parse_args()

    version = "1.0"
    parser.add_argument('variable_length', type=int, help='Length of variable being passed')
    parser.add_argument('line_length', type=int, help='Total length of line, including variable and spaces')
    padding = int
    if (line_length > variable_length): 
        padding = line_length - variable_length
    else:
        print("\nERROR: args[0] must be less than args[1]\n")
        break

    return padding
