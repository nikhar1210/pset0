#!/usr/bin/env python3
"""Print a pyramid to the terminal

A pyramid of height 3 would look like:

--=--
-===-
=====

"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter


def print_pyramid(rows):
    """Print a pyramid of a given height

    :param int rows: total height
    """
    # Calculating total number of '=' signs required
    k = 2 * rows - 1

    # First loop that will iterate over each row of pyramid
    for i in range(rows):

        # Calculating number of '-' sign required on each side of '='
        n = int((k - 1) / 2)

        # Print '-' for left side of pyramid
        for a in range(n):
            print(end="-")

        # Print '=' for each row
        # Calculation for number of '=' equals to (2*number of rows)-1 here row number is i+1
        for b in range(0, ((i + 1) * 2) - 1):
            print(end="=")

        # Print '-' for right side of the row
        for a in range(n):
            print(end="-")

        # Print change of line at the end of row
        print(end="\n")

        # Reduce value of k by 2 as it is corresponsding to number of '-' which decreasing in each subsequent row
        k = k - 2


if __name__ == "__main__":
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument("-r", "--rows", type=int, default=10, help="Number of rows")

    args = parser.parse_args()
    print_pyramid(args.rows)
