#!python
# -*- coding: utf-8 -*-

'''Utilities for preprocessing tags from flair

reference: https://huggingface.co/flair/pos-english
'''

''' A dictionary that maps Flair tags to English parts of speech

TODO maybe make the parts of speech an enumerated type
Also this might be better stored in a CSV
'''
TAG_TO_POS_EN: dict = {
    'ADD':  'NOUN',     # Email
    'AFX':  'OTHER',    # Affix
    'CC':   'CONJUNCTION',  # Coordinating Conjunction
    'CD':   'DETERMINER',   # Cardinal number
    'DT':   'DETERMINER',   # Determiner
    'EX':   'ADVERB',       # Existential there
    'FW':   'OTHER',        # Foreign Word
    'HYPH': 'OTHER',        # Hyphen
    'IN':   'PREPOSITION',  # Preposition or Subordinating Conjunction
    'JJ':   'ADJECTIVE',    # Adjective
    'JJR':  'ADJECTIVE',    # Adjective, superlative
    'JJS':  'ADJECTIVE',    # Adjective, superlative
    'LS':   'DETERMINER',   # List item marker
    'MD':   'VERB',     # Modal
    'NFP':  'OTHER',    # Superfluous punctuation
    'NN':   'NOUN',     # Noun, singular or mass
    'NNP':  'NOUN',     # Proper noun, singular
    'NNPS': 'NOUN',     # Proper noun, plural
    'NNS':  'NOUN',     # Noun, plural
    'PDT':  'DETERMINER',   # Predeterminer TODO review
    'POS':  'OTHER',        # Possessive ending TODO review, maybe add a feature of posessiveness
    'PRP':  'PRONOUN',      # Personal pronoun
    'PRP$': 'PRONOUN',      # Possessive pronoun
    'RB':   'ADVERB',       # Adverb
    'RBR':  'ADVERB',       # Adverb, Comparative
    'RBS':  'ADVERB',       # Adverb, Superlative
    'RP':   'PARTICLE',     # Particle
    'SYM':  'OTHER',        # Symbol
    'TO':   'PARTICLE',     # To
    'UH':   'OTHER',        # Interjection
    'VB':   'VERB',     # Verb, base form
    'VBD':  'VERB',     # Verb, past tense
    'VBG':  'VERB',     # Verb, gerund or present participle
    'VBN':  'VERB',     #Verb, past participle
    'VBP':  'VERB',     # Verb, non-3rd person singular present
    'VBZ':  'VERB',     # Verb, 3rd person singular present
    'WDT':  'DETERMINER',   # Wh-determiner
    'WP':   'DETERMINER',   # Wh-pronoun
    'WP$':  'PRONOUN',      # Possessive wh-pronoun
    'WRB':  'ADVERB',       # Wh-adverb
    'XX':   'OTHER'      # Unknown
}