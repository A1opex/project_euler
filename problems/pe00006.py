#! /usr/bin/python
# coding=utf-8

__author__ = 'a1opex'

from base import ProblemBase


class Problem(ProblemBase):
    """
    The sum of the squares of the first ten natural numbers is,

    12 + 22 + ... + 102 = 385
    The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)2 = 552 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    """

    index = 6
    name ="Sum square difference"

    def main(self):
        return self.sqares(100)

    def sqares(self, n):
        return sum(range(1, n+1)) ** 2 - sum(i ** 2 for i in xrange(1, n+1))