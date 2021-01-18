import datetime
import sys


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform

def get_number(param):
    return range(1 if param else 0, 100, 2)

def excep_func():
    if(1 > 0):
        raise Exception('Example exception')