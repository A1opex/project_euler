#! usr/bin/python
# encoding=utf-8

__author__ = 'a1opex'

from base import ProblemBase

class Problem(ProblemBase):
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    """

    index = 10
    name = "Summation of primes"

    def main(self):
        pri = self.prime(2000000)
        sum = 0
        for i in pri:
            sum += i
        return sum

    def prime(self, n):
        pri = []
        p = [0] * n
        for i in range(2, n):
            if not p[i]:
                for j in range(i + i, n, i):
                    p[j] = 1

        for i in xrange(2, n):
            if not p[i]:
                pri.append(i)
        return pri