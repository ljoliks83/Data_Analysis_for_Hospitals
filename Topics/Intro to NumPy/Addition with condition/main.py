import numpy as np

one_list_warning = "One argument is a list"
two_lists_warning = "Both arguments are lists, not arrays"

def custom_sum(arg1, arg2):
    i = 0
    for arg in (arg1, arg2):
        if isinstance(arg, list):
            i += 1
    if i == 0:
        return arg1 + arg2
    if i == 1:
        return one_list_warning
    if i == 2:
        return two_lists_warning

