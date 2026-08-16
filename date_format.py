#!/usr/bin/env python3
import argparse
import sys
import time
import re
from datetime import datetime, date

# Master dictionary of supported formats
FORMATS = {
    "%a": "Weekday, short version (Wed)",
    "%A": "Weekday, full version (Wednesday)",
    "%b": "Month name, short version (Dec)",
    "%B": "Month name, full version (December)",
    "%c": "Locale date/time (Tue Feb 18 00:00:00 2025)",
    "%d": "Day of month (31)",
    "%D": "Equivalent to %m/%d/%y",
    "%f": "Microsecond 000000-999999",
    "%F": "Equivalent to %Y-%m-%d",
    "%H": "Hour 00-23",
    "%I": "Hour 01-12",
    "%g": "ISO year (2-digit)",
    "%j": "Day number of year 001-366",
    "%m": "Month as number 01-12",
    "%M": "Minute 00-59",
    "%y": "Year, short version",
    "%Y": "Year, full version",
    "%p": "AM/PM",
    "%S": "Second 00-59",
    "%T": "Time in 24-hour notation",
    "%u": "Day of week 1–7",
    "%U": "Week number 00–53",
    "%w": "Weekday 0–6",
    "%x": "Locale date",
    "%X": "Locale time",
    "%z": "UTC offset",
    "%Z": "Timezone",

    # Added so default works
    "%Y%m%d": "Full date (YYYYMMDD)",

    # Custom formats
    "YMD": "Custom Full Date (YYYYMMDD)",
    "YMD_HMS": "Custom Full DateTime (YYYYMMDD.HHMMSS)",
    "YMD_HMS_MS": "Custom Full DateTime with Milliseconds (YYYYMMDD.HHMMSS.mmm)",
}

# Groups for special handling
TIME_RELATED = {"%H", "%I", "%M", "%S", "%T", "%x", "%X", "%z", "%Z"}
MISC_RELATED = {"%f"}
CUSTOM_RELATED = {"YMD", "YMD_HMS", "YMD_HMS_MS"}


def format_custom(key: str) -> str:
    """Handle custom formats not supported directly by strftime."""
    now = datetime.now()

    if key == "YMD":
        return now.strftime("%Y%m%d")

    if key == "YMD_HMS":
        return now.strftime("%Y%m%d.%H%M%S")

    if key == "YMD_HMS_MS":
        ms = now.strftime("%f")[:3]
        return now.strftime("%Y%m%d.%H%M%S.") + ms

    return ""


def print_format(fmt_key: str):
    """Print the formatted date/time for a given key."""
    today = date.today()

    if fmt_key in CUSTOM_RELATED:
        print(format_custom(fmt_key))
        return

    if fmt_key in TIME_RELATED:
        print(time.strftime(fmt_key))
        return

    if fmt_key in MISC_RELATED:
        raw = datetime.now().strftime(fmt_key)
        if fmt_key == "%f":
            print(raw[:3])
        else:
            print(raw)
        return

    print(today.strftime(fmt_key))


def list_formats():
    """Pretty-print all available formats."""
    print("\nAvailable Format Options:\n")
    for key, desc in FORMATS.items():
        print(f"  {key:<12} : {desc}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Return today's date in a specified format."
    )

    # IMPORTANT: --list must be defined BEFORE --format
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all available format options."
    )

    parser.add_argument(
        "--format",
        type=str,
        default="%Y%m%d",
        help="Specify a date/time format key.\nUse --list to view all available format options.\nExample: --format %%a"
    )

    args = parser.parse_args()

    if args.list:
        list_formats()
        sys.exit(0)

    fmt = args.format

    if fmt not in FORMATS:
        print(f"\nERROR: '{fmt}' is not a valid option.\n")
        list_formats()
        sys.exit(2)

    print_format(fmt)


if __name__ == "__main__":
    main()
