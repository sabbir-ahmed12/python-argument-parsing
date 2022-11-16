"""
Counts the number of times an argument flag  is passed.
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="display a square of a given number")
parser.add_argument("-v", "--verbose", action="count", default=0, help="increase output verbosity")

args = parser.parse_args()
ans = args.square ** 2

if args.verbose >=2:
    print(f"Square of {args.square} is {ans}")
elif args.verbose >= 1:
    print(f"{args.square}^2 = {ans}")
else:
    print(ans)
