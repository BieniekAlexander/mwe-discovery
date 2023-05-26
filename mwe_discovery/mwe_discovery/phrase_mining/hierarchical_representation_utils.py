#!python
# -*- coding: utf-8 -*-

"""
This module contains utilities for hierarchical representations in frequent pattern growth algorithms
"""

from collections.abc import Iterable
from typing import Union, Callable, Any
from mwe_discovery.phrase_mining.data_structure_utils import sublist_checker

from enforce_typing import enforce_types
from mwe_discovery.phrase_mining.fhptree import FHPTree

import logging

logger = logging.getLogger()
# logger.setLevel(logging.INFO)


########################
# Candidate Generators #
########################
@enforce_types
def candidate_generator_from_tree(tree: FHPTree, stop_items: Iterable) -> Callable[[Iterable, Any], Iterable]:
    '''Get a candidate generator function, given a [tree] and [stop_items]'''
    @enforce_types
    def _item_candidate_generator(pattern: Iterable, supported_item: str) -> Iterable:
        assert supported_item in tree.get_values()

        token_forms = (
            [supported_item] if supported_item in stop_items
            else [supported_item, *tree.get_ancestors(supported_item)]
        )

        for token_form in token_forms:
            yield (token_form, *pattern)
            yield (*pattern, token_form)

    return _item_candidate_generator


# TODO redundant implementation of a_priori because of some things I'm struggling to handle
@enforce_types
def a_priori(
        corpus: Iterable, # should be generator
        supported_tokens: Iterable,
        stop_tokens: Iterable,
        candidate_generator: Callable[[Any, Any], list], # takes (pattern, supported_token)
        pattern_checker: Callable[[Any, Any], bool], # takes (candidate, document)
        min_support: Union[int, float], # should be integer or float
        ) -> list:    
    """Get the frequent patterns from a corpus, given the supported tokens and stop tokens
    
    TODO maybe update naming to reflect stop_tokens support
    TODO I'm making another implementation of this algorithm to make sure I can perform this algorithm with tuples - make the dedicated implementation generalize well enough to cover tuples

    Args:
        corpus (Iterable): _description_
        stop_tokens (list): _description_
        candidate_generator (function): _description_
        pattern_checker (function): _description_

    Returns:
        list: a list of the frequent patterns
    """
    pattern_appearances = {}

    for i in range(len(corpus)): # TODO this assumes string, make it more general
        document = corpus[i]

        for token in document:
            if token in supported_tokens:
                if (token,) in pattern_appearances:
                    pattern_appearances[token,] |= {i}
                else:
                    pattern_appearances[token,] = {i}

    candidates = list((c,) for c in (set(supported_tokens) - set(stop_tokens)))

    if type(min_support) is float:
        min_support = int(min_support*len(corpus))

    while len(candidates) > 0:
        new_pattern_appearances = {}

        for pattern in candidates:
            for supported_token in supported_tokens:
                for new_candidate in candidate_generator(pattern, supported_token):
                    if new_candidate not in new_pattern_appearances:
                        # get the indexes at which the pattern is present
                        component_indexes = list(set(pattern_appearances.get(pattern, [])) & set(pattern_appearances.get((supported_token,), [])))
                        
                        if len(component_indexes)>=min_support:
                            indexes = [i for i in component_indexes if pattern_checker(new_candidate, corpus[i])]

                            if len(indexes) > min_support:
                                print(new_candidate)
                                new_pattern_appearances[new_candidate] = indexes

        candidates = list(new_pattern_appearances.keys())
        pattern_appearances.update(new_pattern_appearances)

    pattern_appearances = {k: list(pattern_appearances[k]) for k in pattern_appearances}
    return pattern_appearances