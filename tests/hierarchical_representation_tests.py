#!python
# -*- coding: utf-8 -*-

"""
This module contains implementations of the FP-growth algorithm, along with related utilities
"""

from mwe_discovery.phrase_mining.data_structure_utils import sublist_checker

# for pair in [
#         ((corpus[0][1],), corpus[0][0]),
#         ((corpus[0][0],), corpus[0][1]),
# ]:
#      candidates = tuple(item_candidate_generator(*pair),)
#      print(f"{pair} -> {candidates}")
     
#      for cand in candidates:
#         print(f"in first sentence? {sublist_checker(cand, corpus[0])}")