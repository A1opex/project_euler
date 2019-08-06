#!/usr/bin/python

import os
import inspect
from base import ProblemBase


def find_problems():
    """
    Find all problem classes derived from ProblemBase

    :return: A list of ProblemBase
    :rtype: list
    """
    problem_list = []
    current_dir = os.path.dirname(os.path.abspath(__file__))
    for filename in os.listdir(current_dir):
        if not filename.endswith(".py"):
            continue

        module_name = filename[0:-3]
        if module_name.startswith("__"):
            continue

        module = __import__(module_name, globals(), locals())
        for name, mod in inspect.getmembers(module):
            if inspect.isclass(mod) and issubclass(mod, ProblemBase):
                if mod is not ProblemBase:
                    yield mod


__all__ = list(find_problems())
