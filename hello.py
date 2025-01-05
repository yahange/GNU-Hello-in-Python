# -*- coding: utf-8 -*-
#
# GNU Hello in Python
# Copyright (C) 2025 yahange
#
# Description:
# This is a Python implementation oof the GNU Hello program, designed to provide
# a friendly, customizable greeting from the command line. It supports multiple
# options including displaying the version, using a traditional greeting, and
# customizing the greeting message. This project follows the GNU General Public
# License and serves as a learning tool for Python command-line programming.
#
# Copyright and License Details:
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# For more information, contact: yahange@126.com


import argparse
import sys


class RequireValue(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not values:
            parser.error(f"hello: option requires an argument -- '{option_string}'")
        setattr(namespace, self.dest, values)


def display_copyright():
    """Display copyright information in the terminal."""
    print("GNU Hello in Python  Copyright (C) 2025 yahange")


def main():
    if sys.stdin.isatty():
        display_copyright()

    parser = argparse.ArgumentParser(
        description="Print a friendly, customizable greeting."
    )

    parser.add_argument(
        "-v", "--version", action="version", version="GNU Hello 2.10 in Python"
    )

    parser.add_argument(
        "-t", "--traditional", action="store_true", help="use traditional greeting"
    )

    parser.add_argument(
        "-g",
        "--greeting",
        action=RequireValue,
        metavar="TEXT",
        help="use TEXT as the greeting message",
    )

    args = parser.parse_args()

    if args.traditional:
        print("hello, world")
    elif args.greeting:
        print(args.greeting)
    else:
        print("Hello, world!")


if __name__ == "__main__":
    main()
