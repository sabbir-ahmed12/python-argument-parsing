"""
Integer Positional Argument Parser
"""

import argparse

parser = argparse.ArgumentParser()
# python integer_arg <an int>
parser.add_argument("square", help="displays the square of a given number", type=int)
args = parser.parse_args()

print(args.square ** 2)
