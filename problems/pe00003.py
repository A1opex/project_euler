#! /usr/bin/python

from base import ProblemBase

__author__ = 'a1opex'

class Problem(ProblemBase):
    """
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    """

    index = 3
    name = "Largest prime factor"

    def main(self):
        pri = self.prime(1000000)
        to = 600851475143
        flag = 1
        for i in pri:
            if (to % i) == 0:
                if i > flag:
                    flag = i
                to = to / i
        return flag

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