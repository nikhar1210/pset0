#!/usr/bin/env python3


def last_8(some_int):
    """Return the last 8 digits of an int

    :param int some_int: the number
    :rtype: int
    """
    # Adding exception handeling for input values not integers
    if not isinstance(some_int, int):
        raise TypeError

    # Adding exception for negative values
    if some_int < 0:
        raise ValueError

    # For integers with length less than 8, return number as it is
    if (len(str(some_int))) < 8:
        return some_int

    # For integers greater than 8 convert the number to string take the length
    # then return number from length - 8 through last digits
    else:
        return int(str(some_int)[len(str(some_int)) - 8 : len(str(some_int))])


def optimized_fibonacci(n):

    # Exception handeling for input not an integer
    if not isinstance(n, int):
        raise TypeError

    # Exception handeling for input less than 0
    if n < 0:
        raise ValueError

    # Initializing fibonacci by declaring starting values
    a, b = 0, 1

    # Loop which will run for n times and value of "a" will give us nth term in fibonacci sequence
    for i in range(n):
        temp_a = a
        a = b
        b = temp_a + b
    return a


class SummableSequence:
    def __init__(self, a, b, c=None):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, i):
        termA, termB, termC = self.a, self.b, self.c

        if termC is None:
            for j in range(i):
                temp_a = termA
                termA = termB
                termB = temp_a + termB

            return termA

        if termC is not None:

            for j in range(i):
                temp_a = termA
                temp_b = termB
                termA = termB
                termB = termC
                termC = temp_a + temp_b + termC
            return termA


if __name__ == "__main__":

    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))

    new_seq = SummableSequence(5, 7, 11)
    print("new_seq(100000)[-8:]:", last_8(new_seq(100000)))
