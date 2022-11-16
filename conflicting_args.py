"""
Takes one argument at a time not both.
"""
import argparse

parser = argparse.ArgumentParser(description="Calculate X to the power Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="base")
parser.add_argument("y", type=int, help="exponent")

# python conflicting_args.py <base> <exp> -v/-q/<nothing>

args = parser.parse_args()
ans = args.x ** args.y

if args.quiet:
    print(ans)
elif args.verbose:
    print(f"{args.x}^{args.y} equals to {ans}")
else:
    print(f"{args.x}^{args.y} = {ans}")
