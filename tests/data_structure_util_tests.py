#!python
# -*- coding: utf-8 -*-

"""
This module contains implementations of the FP-growth algorithm, along with related utilities
"""

from mwe_discovery.phrase_mining.data_structure_utils import sublist_checker


def test_sublist_checker_success_empty():
    '''Tests if the sublist checker succeeds if the sublist is empty'''
    assert sublist_checker([], list(range(5)))


def test_sublist_checker_success_start():
    '''Tests if the sublist checker succeeds if the sublist is empty'''
    assert sublist_checker([0,1], list(range(5)))


def test_sublist_checker_success_middle():
    '''Tests if the sublist checker succeeds if the sublist is empty'''
    assert sublist_checker([2,3], list(range(5)))


def test_sublist_checker_success_end():
    '''Tests if the sublist checker succeeds if the sublist is empty'''
    assert sublist_checker([3,4], list(range(5)))


def test_sublist_checker_success_singleton_start():
    '''Tests if the sublist checker succeeds if the sublist is empty'''
    assert sublist_checker([0], list(range(5)))


def test_sublist_checker_success_singleton_middle():
    '''Tests if the sublist checker succeeds if the sublist is empty'''
    assert sublist_checker([2], list(range(5)))


def test_sublist_checker_success_singleton_middle():
    '''Tests if the sublist checker succeeds if the sublist is empty'''
    assert sublist_checker([4], list(range(5)))


def test_sublist_checker_success_singleton_absent():
    '''Tests if the sublist checker succeeds if the sublist is empty'''
    assert not sublist_checker([5], list(range(5)))


def test_sublist_checker_success_list_absent():
    '''Tests if the sublist checker succeeds if the sublist is empty'''
    assert not sublist_checker([5,1], list(range(5)))


def test_sublist_checker_success_list_absent_partial():
    '''Tests if the sublist checker succeeds if the sublist is empty'''
    assert not sublist_checker([0, 5], list(range(5)))


def test_sublist_checker_success_list_absent_partial_start():
    '''Tests if the sublist checker succeeds if the sublist is empty'''
    assert not sublist_checker([0, 5], list(range(5)))


def test_sublist_checker_success_list_absent_partial_middle():
    '''Tests if the sublist checker succeeds if the sublist is empty'''
    assert not sublist_checker([2, 5], list(range(5)))


def test_sublist_checker_success_list_absent_partial_end():
    '''Tests if the sublist checker succeeds if the sublist is empty'''
    assert not sublist_checker([4, 5], list(range(5)))