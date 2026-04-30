#!/usr/bin/env python3
"""
Timezone CLI Tool

A simple command-line tool for converting time between different timezones.
"""

import argparse
import sys
from datetime import datetime
import pytz


def main():
    parser = argparse.ArgumentParser(description="Convert time between timezones.")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # 'now' command
    parser_now = subparsers.add_parser('now', help='Show current time in a timezone')
    parser_now.add_argument('--to', required=True, help='Target timezone (e.g., America/New_York)')

    # 'convert' command
    parser_convert = subparsers.add_parser('convert', help='Convert a specific time between timezones')
    parser_convert.add_argument('time', help='Time to convert (format: YYYY-MM-DD HH:MM)')
    parser_convert.add_argument('--from', required=True, dest='from_tz', help='Source timezone (e.g., Asia/Shanghai)')
    parser_convert.add_argument('--to', required=True, help='Target timezone (e.g., Europe/London)')

    # 'list' command
    parser_list = subparsers.add_parser('list', help='List common timezones')
    parser_list.add_argument('--continent', help='Filter by continent (e.g., America, Europe, Asia)')

    args = parser.parse_args()

    if args.command == 'now':
        show_now(args.to)
    elif args.command == 'convert':
        convert_time(args.time, args.from_tz, args.to)
    elif args.command == 'list':
        list_timezones(args.continent)
    else:
        parser.print_help()


def show_now(target_tz):
    try:
        tz = pytz.timezone(target_tz)
        now = datetime.now(tz)
        print(now.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
    except pytz.exceptions.UnknownTimeZoneError:
        print(f"Error: Unknown timezone '{target_tz}'", file=sys.stderr)
        sys.exit(1)


def convert_time(time_str, from_tz, to_tz):
    try:
        from_zone = pytz.timezone(from_tz)
        to_zone = pytz.timezone(to_tz)
    except pytz.exceptions.UnknownTimeZoneError as e:
        print(f"Error: Unknown timezone - {e}", file=sys.stderr)
        sys.exit(1)

    try:
        naive = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
        localized = from_zone.localize(naive)
        converted = localized.astimezone(to_zone)
        print(converted.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
    except ValueError:
        print("Error: Invalid time format. Use YYYY-MM-DD HH:MM", file=sys.stderr)
        sys.exit(1)


def list_timezones(continent=None):
    all_timezones = pytz.all_timezones
    if continent:
        filtered = [tz for tz in all_timezones if tz.startswith(continent + '/')]
        for tz in sorted(filtered):
            print(tz)
    else:
        # Group by continent
        continents = {}
        for tz in all_timezones:
            if '/' in tz:
                cont = tz.split('/')[0]
                continents.setdefault(cont, []).append(tz)
            else:
                continents.setdefault('Other', []).append(tz)

        for cont in sorted(continents.keys()):
            print(f"{cont}:")
            for tz in sorted(continents[cont]):
                print(f"  {tz}")
            print()


if __name__ == '__main__':
    main()