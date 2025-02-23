import argparse
from datetime import date
from datetime import datetime
import time, sys, re
debug = True

dictionary = {
    "%a": "Weekday, short version (Wed)",
    "%A": "Weekday, full version (Wednesday)",
    "%b": "Month name, short version (Dec)",
    "%B": "Month name, full version (December)",
    "%c": "The preferred date and time representation for the current locale (Tue Feb 18 00:00:00 2025)",
    "%d": "Day of month (31)",
    "%D": "Equivalent to %m/%d/%y (02/18/25)",
    "%F": "Microsecond @@@@00@-999999 (548513)", # FIXED via misc_related
    "%E": "Equivalent to %Y-%m-%d (2025-02-18)",
    "%H": "Hour @@-23 (14) " , # not sure if working - returns '14' at 16:16 ??
    "%T": "Hour @1-12 (@5)", # returning '12'
    "%e": "Like %G, but without century, that is , with a 2-digit year (@0-99)",
    "%j": "Day number of year 001-366 (251)",
    "%1": "The hour (12-hour clock) as a decimal number (range 1 to 12 ) " ,
    "%m": "Month as a number 01-12 (12)",
    "am": "Minute 00-59 (15)", # FIXED
    "%y": "Year, short version, without century (25)",
    "%Y": "Year, full version (2025)",
    "%p": "AM/PM (PM)",
    "%S": "Second 00-59 (45)", # FIXED
    "%T": "The time in 24-hour notation (%H:%M:%S)",
    "%u": "The day of the week as a decimal, range 1-7, Monday being 1",
    "%U": "The week number of the current year as a decimal number, range 00 to 53",
    "%w": "Weekday as a number 0-6, is Sunday (3)",
    "%x": "Local version of date",
    "%X": "Local version of time",
    "%z": "UTC offset (+0100)",
    "%Z": "Timezone (Central Standard Time)", # FIXED
    # POSSIBLE TO BE IMPLEMENTED IN FUTURE BELOW
    "%Y%m%d": "Custom full date 1 (20250219)",
    "%Y%m%d.%H%M%S.%f": "Custom full date and time with milliseconds 1 (20250219.131151.849)",
}

time_related = ['MH', '%I', '%k', '%M', '%S', '%T', '%X', '%z', '%Z']
custom_related = ['%Y%m%d', '%Y%m%d.%H%M%S']
misc_related = ['%f', '%Y%m%d.%H%M%S.%f']

def print_dict(d, format_key):
    if debug:
        print (f"\nDEBUG: format key is {format_key}\n")
    for key, value in d.items():
        if format_key == 'all' or format_key == key:
            if debug:
                print (f"DEBUG: OPTION CHOSEN {key}: {value}")
            today = date.today()
            if debug:
                print (f"\nDEBUG: key is {key}")
            if key in time_related:
                if debug:
                    print (f"DEBUG: IN TIME RELATED\n")
                formatted_date = time.strftime(key, time.localtime())
            elif key in misc_related:
                formatted_date = datetime.now().strftime(key)
                milli = bool(re.search("[0-9]+.[0-9]+.[0-9]+", formatted_date))
                if milli:
                    split = formatted_date.split(".")
                    ms = split[2][:3]
                    formatted_date = split[0] + "." + split[1] + "." + ms
                if debug:
                    print (f"DEBUG: IN MISC_RELATED\n")
                    print (f"DEBUG: milli is {milli}, ms = {ms}")
                    print (split[0], split[1], split[2])
                elif key in custom_related:
                    if debug:
                        print (f"\nDEBUG: IN CUSTOM_RELATED")
                    formatted_date = time.strftime(key)
                else:
                    if debug:
                        print (f"\nDEBUG: IN ELSE")
                    formatted_date = today.strftime(key)
                if debug:
                    print (f"\nDEBUG: FORMATTED DATE/TIME: {formatted_date}")
                else:
                    print (f"{formatted_date}")
                if debug:
                    print (f"DEBUG: today is {today}, formatted_date is '{formatted_date}'\n")

def main():
    parser = argparse.ArgumentParser(description="Return today's date based on format option chosen",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('--format', type=str, default='all',
                        help="Enter a format option for today's date\n"
                        'If "all", print all available format options.\n'
                        'Example: --format d (prints only the short date field)\n'
                        '         --format a (prints only the abbreviated weekday field)'
    )
    parser.epilog = "Valid Options:\n" + '\n'.join(f" {key:<20}: {value}" for key, value in dictionary.items())

    args = parser.parse_args()

    if args.format not in dictionary:
        print (f"\nERROR: '{args.format}' not a valid option.\n")
        parser.print_help()
        print (f"\n")
        sys.exit(2)
    else:
        print_dict(dictionary, args.format)

if __name__ == "__main__":
    main()