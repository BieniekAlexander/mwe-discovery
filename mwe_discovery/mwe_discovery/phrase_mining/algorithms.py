#!python
# -*- coding: utf-8 -*-

"""
This module contains implementations of Frequent Pattern Mining algorithms, along with related utilities
"""

import logging
from collections.abc import Iterable
from typing import Any, Callable, Union, Dict, List

from enforce_typing import enforce_types


######################################
# Frequent Pattern Mining Algorithms #
######################################
@enforce_types
def a_priori(
        corpus: Iterable, # should be generator
        supported_tokens: Iterable,
        stop_tokens: Iterable,
        candidate_generator: Callable[[Any, Any], Iterable], # takes (pattern, supported_token)
        pattern_checker: Callable[[Any, Any], bool], # takes (candidate, document)
        min_support: Union[int, float],
        ) -> Dict[Any, List[int]]:
    """
    Get the frequent patterns from a corpus, given the supported tokens and stop tokens
    
    TODO maybe update naming to reflect stop_tokens support

    Args:
        corpus (Iterable): _description_
        supported_tokens (Iterable): _description_
        stop_tokens (Iterable): _description_
        candidate_generator (Callable[[Any, Any], Iterable]): _description_
        pattern_checker (Callable[[Any, Any], bool]): _description_
        min_support (Union[int, float]): _description_
        
    Returns:
        dict[Any, list[int]]: a list of the frequent patterns
    """
    pattern_appearances = {}

    for i in range(len(corpus)): # TODO this assumes string, make it more general
        document = corpus[i]

        for token in document.split(' '):
            if token in pattern_appearances:
                pattern_appearances[token] |= {i}
            else:
                pattern_appearances[token] = {i}

    for key in set(pattern_appearances.keys()) - set(supported_tokens):
        pattern_appearances.pop(key)

    # pattern_appearances = { # TODO update naming
    #     pattern: list(filter(lambda i: pattern_checker(pattern, corpus[i]), range(len(corpus)))) # TODO forcing tuple key, see blow TODO
    #     for pattern in supported_tokens
    # }

    # TODO I modified this function to ,ake sure that candidate generation worked for tuples, but it'll probably break for strings - fix
    candidates = list((set(supported_tokens) - set(stop_tokens)))

    if type(min_support) is float:
        min_support = int(min_support*len(corpus))

    while len(candidates) > 0:
        new_pattern_appearances = {}

        for pattern in candidates:
            for supported_token in supported_tokens:
                results = candidate_generator(pattern, supported_token)
                for new_candidate in results:
                    if new_candidate not in new_pattern_appearances:
                        # get the indexes at which the pattern is present
                        component_indexes = list(set(pattern_appearances.get(pattern, [])) & set(pattern_appearances.get(supported_token, [])))
                        
                        if len(component_indexes)>=min_support:
                            indexes = [i for i in component_indexes if pattern_checker(new_candidate, corpus[i])]

                            if len(indexes) > min_support:
                                new_pattern_appearances[new_candidate] = indexes

        candidates = list(new_pattern_appearances.keys())
        pattern_appearances.update(new_pattern_appearances)

    pattern_appearances = {k: list(pattern_appearances[k]) for k in pattern_appearances}
    return pattern_appearances