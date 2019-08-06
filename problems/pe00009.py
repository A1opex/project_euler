#! usr/bin/python
# encoding=utf-8

__author__ = 'a1opex'

from base import ProblemBase

class Problem(ProblemBase):
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a2 + b2 = c2
    For example, 32 + 42 = 9 + 16 = 25 = 52.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """

    index = 9
    name = "Special Pythagorean triplet"

    def main(self):
        for a in range(1, 499):
            for b in range(499, 1, -1):
                c = 1000 - a - b
                a2 = a ** 2
                b2 = b ** 2
                c2 = c ** 2
                if ((a2 + b2) == c2):
                    return a*b*c
