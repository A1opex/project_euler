#!/usr/bin/python
# -*- coding=utf-8 -*-


"""
Main entry of Project Euler problems

Author: Flily Hsu(flily.hsu@qq.com)
"""

import sys
import logging
from argparse import ArgumentParser

import base
import problems


def list_problems(patterns):
    """
    List problems.

    :param patterns: Patterns for problems.
    :return:
    """
    for p in problems.find_problems():
        if not patterns:
            print "[%s] %s" % (p.index, p.name)

        else:
            base_info = [
                str(p.index),
                str(p.name.lower()),
                str(p.get_description().lower()),
            ]

            for x in patterns:
                is_matched = False
                for b in base_info:
                    if x in b:
                        is_matched = True

                if is_matched:
                    print "[%s] %s" % (p.index, p.name)


def show_problem(patterns):
    """
    Show description of problems.

    :param patterns:
    :return:
    """
    for p in problems.find_problems():
        if str(p.index) in patterns:
            print "[%s] %s" % (p.index, p.name)
            print p.get_description()


def run_problem(patterns):
    """
    Run problems.

    :param patterns:
    :return:
    """
    for p in problems.find_problems():
        if str(p.index) in patterns:
            try:
                pi = p()
                assert isinstance(pi, base.ProblemBase)
                pi.solve()

            except NotImplementedError as ex:
                logging.error(ex)


def get_log_format(fmt=""):
    """
    Get logging formatter instance from str.

    :param fmt: Format string.
    :type fmt: str
    :return:
    :rtype: logging.Formatter
    """
    if not fmt:
        fmt = "[%(asctime)s] %(message)s"
        if not isinstance(sys.version_info, tuple):
            # For Python 2.7:
            # Attributes filename and lineno are not supported in Python 2.6.
            fmt = "[%(asctime)s] %(filename)s:%(lineno)d: %(message)s"

    return logging.Formatter(fmt)


def init_logger(debug_mode, filename=""):
    """
    Import logging facilities.
    Log file will not be written when filename is empty.

    :param debug_mode: Is in debug mode.
    :type debug_mode: bool
    :param filename: Filename of log file.
    :type filename: str
    :return:
    """
    logger = logging.getLogger()
    logger.setLevel(logging.NOTSET)

    level = logging.INFO
    if debug_mode:
        level = logging.DEBUG

    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(get_log_format("[%(asctime)s] %(message)s"))
    console.setLevel(level)
    logger.addHandler(console)

    if filename:
        logfile = logging.FileHandler(filename)
        logfile.setFormatter(get_log_format())
        logfile.setLevel(level)
        logger.addHandler(logfile)


def init_options():
    """
    Initialize an ArgumentParser for parsing command-line arguments.

    :return: An instance of ArgumentParser
    :rtype: ArgumentParser
    """
    arg_parser = ArgumentParser()
    arg_parser.add_argument("-d", "--debug", dest="debug_mode",
                            action='store_true', default=False,
                            help="Run as debug mode")
    arg_parser.add_argument("--log", dest="log_file",
                            action="store", default="",
                            help="Filename for logging")
    arg_parser.add_argument("action", metavar="ACTION",
                            help="Action for problems")
    arg_parser.add_argument("pattern", metavar="PATTERN", nargs="*",
                            help="Patterns for problems")
    return arg_parser


def main(args):
    action = args.action
    patterns = args.pattern

    if "list" == action:
        list_problems(patterns)

    elif "show" == action:
        show_problem(patterns)

    elif "run" == action:
        run_problem(patterns)


if __name__ == "__main__":
    arguments = init_options().parse_args()
    init_logger(arguments.debug_mode, arguments.log_file)
    main(arguments)
