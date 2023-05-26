#!python
# -*- coding: utf-8 -*-

'''
This module contains an implementation of a tree data structure used for frequent pattern mining with hierarchical values

Reference: https://mospace.umsystem.edu/xmlui/handle/10355/63867
'''

from enforce_typing import enforce_types
from typing import Any
from collections.abc import Iterable


#############
# Constants #
#############
TREE_ROOT = None


#######################
# Tree Implementation #
#######################
class FHPTree:
    '''A tree allowing for checking hierarchical equality'''

    _mapper = {}

    @enforce_types
    def __init__(self, items: list[Iterable]) -> object:
        '''Constructs a tree from the list of [items]

        Each item in items shall be an Iterable representing the representations of the item,
        from the least specific representation to the most specific representation:
        ('noun', 'animal', 'cat'), for example
        '''
        for item in items:
            for i in range(len(item)):
                field = item[i]
                parent = item[i-1] if i>0 else None

                if field not in self._mapper:
                    self._mapper[field] = parent
                elif self._mapper[field] != parent:
                    raise ValueError(
                        f"""Discrepancy in the hierarchical relatonship represented in tree construction:
                        item: {item}
                        field: {field}
                        parent found in item: {parent}
                        parent found in tree: {self._mapper[field]}{" (ROOT)" if self._mapper[field]==TREE_ROOT else ""}"""
                    )


    @enforce_types
    def get_parent(self, item) -> Any:
        '''Get the direct parent of [item]'''
        if item not in self._mapper:
            raise ValueError(f"item not found in tree: {item}")
        else:
            return self._mapper[item]
        

    @enforce_types
    def get_ancestors(self, item) -> list:
        '''Get all ancestors of [item]'''
        ancestors = []
        key = item

        while key != None:
            value = self.get_parent(key)

            if value != None:
                ancestors.append(self._mapper[key])

            key = value

        return ancestors
    

    @enforce_types
    def get_values(self) -> list:
        '''Gets all items from the tree'''
        return list(self._mapper.keys())