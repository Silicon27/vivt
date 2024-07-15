#!/usr/bin/env python

import argparse
import requests
import os
import vivtfiles.vpl 

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
        
def main():
    parser = argparse.ArgumentParser(description="CLI tool for Vast")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Greet command
    greet_parser = subparsers.add_parser("greet", help="Greet the user when provided the name")
    greet_parser.add_argument("name", type=str, help="Name to greet")

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
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
