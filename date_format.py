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
    "%Y-%m-%d": "ISO date (YYYY-MM-DD)",
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
    "%Y%m%d": "Full date (YYYYMMDD)",
    "YMD": "Custom Full Date (YYYYMMDD)",
    "YMD_HMS": "Custom Full DateTime (YYYYMMDD.HHMMSS)",
    "YMD_HMS_MS": "Custom Full DateTime with Milliseconds (YYYYMMDD.HHMMSS.mmm)",
}

TIME_RELATED = {"%H", "%I", "%M", "%S", "%T", "%x", "%X", "%z", "%Z"}
MISC_RELATED = {"%f"}
CUSTOM_RELATED = {"YMD", "YMD_HMS", "YMD_HMS_MS"}


def build_date_patterns() -> list[str]:
    """Generate common date patterns dynamically from component order and separators."""
    formats = [
        ["%Y", "%m", "%d"],
        ["%m", "%d", "%Y"],
        ["%d", "%m", "%Y"],
        ["%Y", "%d", "%m"],
        ["%b", "%d", "%Y"],
        ["%B", "%d", "%Y"],
    ]

    separators = ["-", "/", " ", ", "]
    patterns = []

    for parts in formats:
        for separator in separators:
            joined = separator.join(parts)
            patterns.append(joined)

    # Compact numeric variants such as 12312001 or 02182025.
    patterns.extend([
        "%Y%m%d",
        "%m%d%Y",
        "%m%d%y",
        "%d%m%Y",
        "%d%m%y",
    ])

    # Add a few explicit common variants that are easy to miss in the dynamic loop.
    patterns.extend([
        "%m-%d-%Y",
        "%m/%d/%Y",
        "%d-%m-%Y",
        "%d/%m/%Y",
    ])

    return patterns


def parse_date_input(value: str) -> date:
    """Parse a user-supplied date from common input formats."""
    if value is None:
        return date.today()

    value = value.strip()
    if not value:
        raise ValueError("Date value cannot be empty.")

    for pattern in build_date_patterns():
        try:
            return datetime.strptime(value, pattern).date()
        except ValueError:
            continue

    raise ValueError(
        f"Unsupported date format: '{value}'. Use ISO (YYYY-MM-DD), compact numeric (MMDDYYYY), US (M/D/YYYY), or natural language like 'Feb 18 2025'."
    )


def format_custom(key: str, target_date: date) -> str:
    """Handle custom formats not supported directly by strftime."""
    dt = datetime.combine(target_date, datetime.min.time())

    if key == "YMD":
        return dt.strftime("%Y%m%d")

    if key == "YMD_HMS":
        return dt.strftime("%Y%m%d.%H%M%S")

    if key == "YMD_HMS_MS":
        ms = dt.strftime("%f")[:3]
        return dt.strftime("%Y%m%d.%H%M%S.") + ms

    return ""


def print_format(fmt_key: str, target_date: date | None = None):
    """Print the formatted date/time for a given key."""
    base_date = target_date or date.today()
    dt = datetime.combine(base_date, datetime.min.time())

    if fmt_key in CUSTOM_RELATED:
        print(format_custom(fmt_key, base_date))
        return

    if fmt_key in TIME_RELATED:
        print(dt.strftime(fmt_key))
        return

    if fmt_key in MISC_RELATED:
        raw = dt.strftime(fmt_key)
        if fmt_key == "%f":
            print(raw[:3])
        else:
            print(raw)
        return

    print(base_date.strftime(fmt_key))


def list_formats():
    """Pretty-print all available formats."""
    print("\nAvailable Format Options:\n")
    for key, desc in FORMATS.items():
        print(f"  {key:<12} : {desc}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Format a date using a selected strftime-style key."
    )

    parser.add_argument(
        "--list",
        action="store_true",
        help="List all available format options."
    )

    parser.add_argument(
        "--date",
        type=str,
        default=None,
        help="Optional date to format instead of today's date. Examples: 2025-02-18, 02/18/2025, Feb 18 2025"
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

    try:
        target_date = parse_date_input(args.date) if args.date else date.today()
        print_format(fmt, target_date)
    except ValueError as exc:
        print(f"\nERROR: {exc}\n")
        sys.exit(2)


if __name__ == "__main__":
    main()
