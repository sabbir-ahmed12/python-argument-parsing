"""
Takes multiple argument values.
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="displays square of a number")
parser.add_argument("-v", "--verbose", type=int, choices=[0, 1, 2], \
                    help="increase output verbosity")

args = parser.parse_args()
ans = args.square ** 2

if args.verbose == 2:
    print(f"The square of {args.square} is {ans}")
elif args.verbose == 1:
    print(f"{args.square}^2 == {ans}")
else: print(ans)
