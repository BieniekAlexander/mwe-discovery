"""
This script prepares and runs time trials for a string search task. In particular, I'm testing the runtime of 
searching for a substring in a primitive string vs a list of strings. It looks like the primitive string search is faster.
"""
from mpmath import mp
from timeit import timeit
from random import randint

LEN = 1000
mp.dps = LEN
pi = mp.pi
pi_string = str(pi)
pi_list = list(pi_string)

def is_substring(sub: list, sup: list):
    """
    Check if [sub] is a substring of [sup]
    """
    if len(sub) == 0: return True
    offset = 0

    while True:
        if sub[0] in sup[offset:] and len(sub) <= len(sup[offset:]):
            offset = sup[offset:].index(sub[0])+offset

            for i in range(1, min(len(sub), len(sup)-offset)):
                if sub[i]!=sup[offset+i]:
                    offset = offset+i
                    break
                elif i==len(sub)-1: # we found a sentence containing the whole substring
                    return True
                
        else:
            return False

index_lens = [(randint(0, LEN-10), randint(2, 5)) for _ in range(10)]
print(index_lens)
search_strings = [pi_string[i:i+l] for (i,l) in index_lens]
search_lists = [pi_list[i:i+l] for (i,l) in index_lens]

COUNT=100
print(f"runtime for string search:\t{timeit(lambda: [search_string in pi_string for search_string in search_strings], number=COUNT)}")
print(f"runtime for list serach:\t{timeit(lambda: [is_substring(search_list, pi_list) for search_list in search_lists], number=COUNT)}")

'''
results:
runtime for string search:      0.00016215200594160706
runtime for list serach:        0.13203276200511027
'''