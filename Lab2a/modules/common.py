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

def odd_even_parity(flag):
    if(flag == "True"):
        var_list = list(range(0,101,2))
    elif(flag == "False"):
        var_list = list(range(1,101,2))
    else:
        print("Error: bad input arg")
        var_list = None
    return var_list