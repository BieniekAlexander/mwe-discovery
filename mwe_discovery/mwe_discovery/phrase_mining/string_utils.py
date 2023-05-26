#!python
# -*- coding: utf-8 -*-

"""
This module contains implementations of the FP-growth algorithm, along with related utilities
"""

import logging
import re
from collections.abc import Iterable
from typing import Any, Callable, Union

from enforce_typing import enforce_types


##########################
# tokenization functions #
##########################
@enforce_types
def get_words(corpus: Iterable) -> set:
    """Get the set of unique words from a corpus of documents"""
    words = set()

    for document in corpus:
        new_words = set(document.split(' '))
        words |= new_words

    words.discard('')
    return words


########################
# Candidate Generators #
########################
@enforce_types
def get_candidate_strings(pattern: str, token: str) -> str:
    """Generates potential candidates coming from a pair of input arguments"""
    return (f"{pattern} {token}", f"{token} {pattern}")


#######################
# Membership Checkers #
#######################
def text_pattern_checker(candidate, document): # TODO better name, and argument types
    """Checks if the candidate pattern is in the document and is not bounded by alphabetical characters"""
    try:
        if re.search(f"(?:^|[^A-Za-z]){candidate}(?:$|[^A-Za-z])", document):
            return True
        else:
            return False
    except:
        raise ValueError(f"failed regex with: '{candidate}' in '{document}'")