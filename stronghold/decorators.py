from functools import partial
from stronghold.utils import set_view_func_public


def public(function):
    """
    Decorator for public views that do not require authentication
    Sets an attribute in the fuction STRONGHOLD_IS_PUBLIC to True
    """
    orig_func = function
    outer_partial_wrapper = None
    while isinstance(orig_func, partial):
        outer_partial_wrapper = orig_func
        orig_func = orig_func.func
    # For Django >= 2.1.x:
    # If `function` is a bound method, django will wrap it in a partial
    # to allow setting attributes on a bound method.
    # Bound methods have the attr "__self__". If this is the case,
    # we reapply the partial wrapper before setting the attribute.
    if hasattr(orig_func, "__self__") and outer_partial_wrapper != None:
        orig_func = outer_partial_wrapper
    set_view_func_public(orig_func)

    return function
