#!/usr/bin/env python3


def last_8(some_int):
    """Return the last 8 digits of an int

    :param int some_int: the number
    :rtype: int
    """

    if (len(str(some_int))) < 8:
        return some_int

    else:

        return int(str(some_int)[len(str(some_int)) - 8 : len(str(some_int))])


if __name__ == "__main__":

    last_8()
