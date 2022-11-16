"""
Takes a positional argument and displays output in different ways
based on optional argument.
"""
import argparse

parser = argparse.ArgumentParser()
# python positional_and_optional_args.py <an int> / <an int> -v / -v <an int>
parser.add_argument("square", type=int, help="display square of a given number")
parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")

args = parser.parse_args()
ans = args.square ** 2

if args.verbose:
    print(f'The square of {args.square} is {ans}')
else:
    print(ans)
