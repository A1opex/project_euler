#!/usr/bin/python
# -*- coding=utf-8 -*-


import abc
import logging


class ProblemBase(object):
    """
    Base class of problems in Project Euler.
    """
    def __init__(self):
        pass

    # Attributes of Problems

    index = 0
    name = "A Project Euler Problem"

    # Abstract methods of Problems

    @abc.abstractmethod
    def main(self):
        """
        Main entry of a problem, return the answer of the problem.

        :return: The answer of this problem.
        :rtype: int
        """
        module_name = self.__class__.__module__
        raise NotImplementedError(
            "Method 'main' not implemented in Problem class '%s'" % module_name
        )

    # Public methods of framework for base class.

    @classmethod
    def get_description(cls):
        """
        Description of a problem.

        :return:
        :rtype: str
        """
        lines = cls.__doc__.split("\n")
        return "\n".join([x.strip() for x in lines])

    def solve(self):
        """
        Start to solve problem.

        :return:
        """
        self.log_debug("Start resolve problem '%s'(%s)", self.index, self.name)
        answer = self.main()
        self.log_debug("Finish problem '%s'", self.index)
        self.log_info("Answer of '%s': %s", self.index, answer)

    def log(self, fmt, *args):
        """
        Log message at default level. (info)

        :param fmt:
        :param args:
        :return:
        """
        self.log_info(fmt, *args)

    def log_error(self, fmt, *args):
        """
        Log message at INFO level.

        :param fmt: Logging format or pattern.
        :type fmt: basestring
        :param args: Arguments to build-up logging message.
        :return: Nothing.
        """
        logging.info(fmt, *args)

    def log_info(self, fmt, *args):
        """
        Log message at INFO level.

        :param fmt: Logging format or pattern.
        :type fmt: basestring
        :param args: Arguments to build-up logging message.
        :return: Nothing.
        """
        logging.info(fmt, *args)

    def log_debug(self, fmt, *args):
        """
        Log message at DEBUG level.

        :param fmt: Logging format or pattern.
        :type fmt: basestring
        :param args: Arguments to build-up logging message.
        :return: Nothing.
        """
        logging.debug(fmt, *args)
