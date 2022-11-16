"""
Displays something based on True/False and this argument is optional
"""

import argparse

parser = argparse.ArgumentParser()
# python optional_arg.py --verbose
parser.add_argument("--verbose", help="displays extra info", action="store_true")
args = parser.parse_args()

if args.verbose:
    print("Verbose set to True")
