#!python
# -*- coding: utf-8 -*-

"""
This module contains utilities related to the standard data structures
"""

from collections.abc import Callable
from typing import Any, Iterable

from enforce_typing import enforce_types


@enforce_types
def sublist_checker(sub: Iterable, sup: Iterable, equality_operation: Callable[[Any, Any], bool] = lambda x, y: x==y) -> bool:
    """Check if [sub] is a sublist of [sup]

    Args:
        sub (Iterable): _description_
        sup (Iterable): _description_
        equality_operation (Callable[[Any, Any], bool], optional): _description_. Defaults to lambdax.
        y (x, optional): _description_. Defaults to =y.

    Returns:
        bool: _description_
    """    
    if len(sub) == 0: return True
    offset = 0

    while offset < len(sup):
        for i in range(len(sub)):
            if offset+i >= len(sup):
                return False
            if not equality_operation(sub[i], sup[offset+i]):
                break
            if i==len(sub)-1:
                return True
            
        offset += 1
    
    return False