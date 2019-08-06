#!/usr/bin/python

from base import ProblemBase


class Problem(ProblemBase):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
     we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    """

    index = 1
    name = "Multiples of 3 and 5"

    def main(self):
        s = 0
        for i in xrange(1, 1000):
            if i % 3 == 0 and i % 5 == 0:
                s += i

        return s
