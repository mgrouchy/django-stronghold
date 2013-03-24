from functools import partial
from stronghold.utils import set_view_func_public


def public(function):
    """
    Decorator for public views that do not require authentication
    Sets an attribute in the fuction STRONGHOLD_IS_PUBLIC to True
    """
    orig_func = function
    while isinstance(orig_func, partial):
        orig_func = orig_func.func
    set_view_func_public(orig_func)

    return function
