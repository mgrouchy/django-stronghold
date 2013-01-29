from functools import partial


def public(function):
    """
    Decorator for public views that do not require authentication
    Sets an attribute in the fuction STRONGHOLD_IS_PUBLIC to True
    """
    orig_func = function
    while isinstance(orig_func, partial):
        orig_func = orig_func.func
    orig_func.STRONGHOLD_IS_PUBLIC = True

    return function
