#!/usr/bin/env python3

from argparse import ArgumentParser, RawDescriptionHelpFormatter

def last_8(some_int):
    """Return the last 8 digits of an int

    :param int some_int: the number
    :rtype: int
    """

    if (len(str(some_int))) < 8:
        return some_int

    else:

        return int(str(some_int)[len(str(some_int)) - 8: len(str(some_int))])


if __name__ == "__main__":

    parser = ArgumentParser(
    description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument("-d", "--digits", type=int, default=12345, help="Number")

    args = parser.parse_args()

    last_8(args.digits)
