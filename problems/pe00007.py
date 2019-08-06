#! usr/bin/python

__author__ = 'a1opex'

from base import ProblemBase


class Problem(ProblemBase):
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10 001st prime number?
    """

    index = 7
    name = "10001st prime"

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

    def main(self):
        pri = self.prime(1000000)
        return pri[10000]