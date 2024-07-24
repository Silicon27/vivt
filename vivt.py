#!/usr/bin/env python

import argparse
import requests
import os
import vivtfiles.vpl

version = "0.1"


class ansic:
    # Text colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    # Bright text colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

    # Bright background colors
    BG_BRIGHT_BLACK = '\033[100m'
    BG_BRIGHT_RED = '\033[101m'
    BG_BRIGHT_GREEN = '\033[102m'
    BG_BRIGHT_YELLOW = '\033[103m'
    BG_BRIGHT_BLUE = '\033[104m'
    BG_BRIGHT_MAGENTA = '\033[105m'
    BG_BRIGHT_CYAN = '\033[106m'
    BG_BRIGHT_WHITE = '\033[107m'

    # Text styles
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINKING = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    STRIKETHROUGH = '\033[9m'


def greet(name):
    print(f"Hello, {name}!")


def requestAPI(code):
    print(f"Requesting API... ({code})")
    print(requests.get(f"https://api.publicapis.org/entries"))


def make_instalation_env() -> None:
    if os.path.exists(".vastlibs/lib/vast/local-packages/"):
        print("\033[31mError: installation environment already exists\033[0m")
    else:
        os.mkdir(".vastlibs")
        print("successfully created lib")
        os.mkdir(".vastlibs/lib")
        print("successfully created lib")
        os.mkdir(".vastlibs/lib/vast")
        print("successfully created vast")
        os.mkdir(".vastlibs/lib/vast/local-packages/")
        print("successfully created local-packages")

        # create the default packages
        os.mkdir(".vastlibs/lib/vast/local-packages/os/")
        print("successfully created os.py")
        os.mkdir(".vastlibs/lib/vast/local-packages/math.py")
        print("successfully created math.py")
        os.mkdir(".vastlibs/lib/vast/local-packages/type.py")

        print("successfully created installation environment")


def get_version() -> None:
    print(f"Vast Integrated Virtual Tool, vivt [Version {ansic.BRIGHT_BLUE + ansic.UNDERLINE + version + ansic.RESET}]")


def main():
    parser = argparse.ArgumentParser(description="CLI tool for Vast")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Greet command
    greet_parser = subparsers.add_parser("greet", help="Greet the user when provided the name")
    greet_parser.add_argument("name", type=str, help="Name to greet")

    # Version command
    version_parser = subparsers.add_parser("version", help="Get the current version of vivt installed on your machine")

    # Request command
    request_parser = subparsers.add_parser("request", help="Request an API call to a website")
    request_parser.add_argument("-u", "--url", type=str, help="Request for an API call")

    create_instalation_env_parser = subparsers.add_parser("mkienv", help="Create an MKI environment")

    args = parser.parse_args()

    if args.command == 'greet':
        greet(args.name)
    elif args.command == 'request':
        requestAPI(args.url)
    elif args.command == 'mkienv':
        make_instalation_env()
    elif args.command == 'version':
        get_version()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
