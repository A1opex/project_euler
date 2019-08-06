#! usr/bin/python
# encoding=utf-8

from base import ProblemBase

__author__ = 'a1opex'

class Problem(ProblemBase):
    """
    The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
    """

    index = 14
    name = "Longest Collatz sequence"

    def sequence(self, n):
        seq = []
        while n > 1:
            seq.append(n)
            if n % 2 == 0:
                n = n/2
            else:
                n = 3*n + 1

        return len(seq)

    def main(self):
        tmp = 0
        the_max = 0
        for i in xrange(1000000):
            l = self.sequence(i)
            if l > tmp:
                tmp = l
                the_max = i
        return the_max