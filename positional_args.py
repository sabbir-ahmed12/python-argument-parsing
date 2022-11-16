'''
Positional argument parsing using argparse.
'''

import argparse

parser = argparse.ArgumentParser()
# python positional_args.py <an arg>
parser.add_argument("echo", help="echo the string passed with command")
args = parser.parse_args()
print(args.echo)
