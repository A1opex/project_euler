#! usr/bin/python
# coding=utf-8

__author__ = 'a1opex'

import math

from base import ProblemBase

class Problem(ProblemBase):
    """
    A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers
    """

    index = 4
    name = "Largest palindrome product"

    def mult(self, x, y, z):
        p = x*100000 + y*10000 + z*1000 + z*100 + y*10 + x
        return p

    def palindromic(self, par):
        flag = int(math.sqrt(par))
        for i in xrange(flag - 1, 1000):
            if par % i == 0:
                div = par / i
                if div >= 100 and div < 1000:
                    print par,div,i
                    return True

    def main(self):
        for x in range(9, -1 ,-1):
            for y in range(9, -1, -1):
                for z in range(9, -1, -1):
                    p = self.mult(x, y, z)
                    if self.palindromic(p):
                        return p