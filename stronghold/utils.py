def is_view_func_public(func):
    """
    Returns whether a view is public or not (ie/ has the STRONGHOLD_IS_PUBLIC
    attribute set)
    """
    return getattr(func, 'STRONGHOLD_IS_PUBLIC', False)


def set_view_func_public(func):
    """
    Set the STRONGHOLD_IS_PUBLIC attribute on a given function to True
    """
    setattr(func, 'STRONGHOLD_IS_PUBLIC', True)
