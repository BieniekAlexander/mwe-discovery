#!python
# -*- coding: utf-8 -*-

"""
This module contains unit tests for the FHPTree
"""

from mwe_discovery.phrase_mining.fhptree import FHPTree
import pytest


@pytest.fixture
def good_tree_data():
    return [
        ('food', 'meat', 'steak'),
        ('food', 'meat', 'chicken'),
        ('food', 'vegetable', 'brocolli'),
        ('drink', 'non-alcoholic', 'water'),
        ('drink', 'alcoholic', 'beer'),
        ('food', 'pantry item', 'flour', 'wheat flour'),
        ('food', 'pantry item', 'flour', 'rye flour'),
        ('food', 'pantry item', 'sugar'),
    ]


#####################
# Constructor Tests #
#####################
def test_construct_fhp_tree_success_good_data(good_tree_data):
    '''Tests that the FHPTree is constructed correctly with good data'''
    FHPTree(good_tree_data)


def test_construct_fhp_tree_success_no_data():
    '''Tests that the FHPTree is constructed correctly with no data'''
    FHPTree([])


def test_construct_fhp_tree_failure_bad_data(good_tree_data):
    '''Tests that the FHPTree fails construction with data representing an incorrect hierarchy'''
    bad_tree_data = good_tree_data + [('drink', 'meat', 'brotein shake')]

    with pytest.raises(ValueError):
        FHPTree(bad_tree_data)


###################
# Get Parent Test #
###################
def test_get_parent_success(good_tree_data):
    '''Tests that the find parent functionality of the tree works as expected'''
    tree = FHPTree(good_tree_data)

    for entry in good_tree_data:
        for i in range(1, len(entry)):
            assert \
                tree.get_parent(entry[i]) == entry[i-1], \
                f"It's not the case that {entry[i-1]} is the parent of {entry[i]}, which conflicts with the input data"

            
def test_get_parent_success_root(good_tree_data):
    '''Tests that the find parent functionality of the tree works when trying to find data at the root'''
    tree = FHPTree(good_tree_data)
    assert tree.get_parent(good_tree_data[0][0]) == None


def test_get_parent_failure_not_found(good_tree_data):
    '''Tests that the find parent functionality fails when nonexistent data is queried'''
    tree = FHPTree(good_tree_data)

    with pytest.raises(ValueError):
        tree.get_parent('I am not in the tree')


######################
# Get Ancestors Test #
######################
def test_get_ancestors_success(good_tree_data):
    '''Tests that the get ancestors functionality of the tree works as expected'''
    tree = FHPTree(good_tree_data)

    for entry in good_tree_data:
        for i in range(1, len(entry)):
            assert \
                set(tree.get_ancestors(entry[i])) == set(entry[:i]), \
                f"It's not the case that {entry[:i]} is the list of ancestors of {entry[i]}, which conflicts with the input data"



def test_get_ancestors_failure_not_found(good_tree_data):
    '''Tests that the get ancestors functionality of the tree fails when querying a non-existent item'''
    tree = FHPTree(good_tree_data)

    with pytest.raises(ValueError):
        tree.get_ancestors('I am not in the tree')


def test_get_ancestors_success_root(good_tree_data):
    '''Tests that the get ancestors functionality of the tree works as expected'''
    tree = FHPTree(good_tree_data)
    assert tree.get_ancestors(good_tree_data[0][0]) == []