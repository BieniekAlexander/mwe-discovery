#!python
# -*- coding: utf-8 -*-

'''Token representation, based on CoNLL-U format

reference: https://universaldependencies.org/format.html
'''
from typing import Optional
from dataclasses import dataclass, field


class HashableDict(dict):
    '''https://stackoverflow.com/a/16162138'''
    def __hash__(self):
        return hash(frozenset(self))


@dataclass(frozen=True, eq=True)
class CoNLLUToken:
    '''Class representing CoNLL-U Tokens
    
    refer to the following for the specification: https://universaldependencies.org/format.html
    '''
    # _id: Union[int, tuple[int, int]]    # Word index, integer starting at 1 for each new sentence; may be a range for multiword tokens; may be a decimal number for empty nodes (decimal numbers can be lower than 1 but must be greater than 0).
    form: Optional[str]=None           # the inflected form of the word, as it appears in the text
    lemma: Optional[str]=None          # lemma form of the word
    upos: Optional[str]=None              # Universal part-of-speech tag
    # xpos: str                           # the part of speech for the specific language
    feats: HashableDict=field(default_factory=HashableDict)         # a list of morphological features from the universal feature inventory, or from defined language-specific extension
    # head: int                           # head of the current word, which is either a value of ID or zero (0)
    # deprel: str                         # universal dependency relation to the HEAD (root iff HEAD = 0) or a defined language-specific subtype of one
    # deps: dict[int,str]                 # enhanced dependency graph in the form of a list of head-deprel pairs
    # misc: str                           # any other annotation


    def __post_init__(self):
        """Postprocess and make sure the [feats] field is a [HashableDict]"""
        object.__setattr__(self, 'feats', HashableDict(self.feats))

    # Defining comparison operators
    def __le__(self, other):
        '''Returns [True] if [self] is a more generic token than [other]'''
        return (
            (self.form is None or self.form == other.form) and 
            (self.lemma is None or self.lemma == other.lemma) and 
            (self.upos is None or self.upos == other.upos) and 
            all(self.feats[key] == other.feats[key] for key in self.feats)
        )
    
    __lt__ = lambda self, other: (self != other and self <= other)
    __ge__ = lambda self, other: (self == other or not (self <= other))
    __gt__ = lambda self, other: not (self <= other)

    # Defining set operators
    def __and__(self, other):
        '''Returns the union of [self] and [other] tokens'''
        return CoNLLUToken(
            form=self.form if self.form==other.form else None,
            lemma=self.lemma if self.lemma==other.lemma else None,
            upos=self.upos if self.upos==other.upos else None,
            feats={
                k: v for k, v in self.feats.items()
                if (k in other.feats and other.feats[k] == v)
            }
        )


if __name__ == '__main__':
    a = CoNLLUToken(form="wow", lemma="no")
    b = CoNLLUToken(form="wow", lemma='oh', feats={1:2, 3:4})
    c=a&b

    print(c)