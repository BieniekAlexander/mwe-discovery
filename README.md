# Introduction
A workspace for the task of mining multiword expressions (MWEs) from a corpus of text.

## Task Overview
In linguistics, lexicalization refers to the imbuing of semantic meaning to a lexeme of a language. As a simple example, the word "went" refers to a lexeme in the English language that discusses motion, and other words encompassed by this lexeme include "goes", "going", and "go". Finally, a dictionary will represent this lexeme with a given form, known as the lemma - in this case, the lemma form of the lexeme is the word "go". Lexically, this concept of "going" might be represented with different inflections of the word, but they semantically represent a consistent idea.

There exists a pattern in natural language use wherein, when speakers combine multiple words into an expression, that expression can take on semantic meanings that extend beyond the ideas represented by the components of the phrase. For example, English speakers commonly use the phrase "go over", and in some cases, this phrase would describe motion over some sort of object. For example, if I were to say "the dog went over the fence", the idea would simply refer to the dog's motion with respect to the fence. However, this same phrase, when used in different contexts, takes on a meaning that effectively has little to do with the individual ideas represented by "go" and "over". As an example, "to go over a text" doesn't speak of motion of an subject - rather, the phrase refers to a subject reviewing something (reviewing a text, in this case). Such expressions have meaning not easily understood by the components of the expression, so it's helpful to identify phrases that have such meaning, especially for language learning tasks. This repository is dedicatred to this task of MWE discovery.

TODO add references to literature and such.

# Usage
## Setup
```bash
# Initial environment setup
CONDA_ENV_NAME=mwe-discovery
conda create --name $CONDA_ENV_NAME python=3.11.3 -y
conda activate $CONDA_ENV_NAME
pip install -r requirements.txt
python -m ipykernel install --user --name=$CONDA_ENV_NAME

# setup python path
export PYTHONPATH=`pwd`
```

## Testing
```bash
pytest --cov phrase_mining tests/*
```

# Resources
## Natural Language
- [Distributional Semantics](https://en.wikipedia.org/wiki/Distributional_semantics)

## Pattern Mining
- [FP Growth Implementation](https://towardsdatascience.com/fp-growth-frequent-pattern-generation-in-data-mining-with-python-implementation-244e561ab1c3)

## Statistics
- [Pointwise Mutual Information](https://en.wikipedia.org/wiki/Pointwise_mutual_information)

## Datasets
- [NLTK's Brown Corpus](https://www.nltk.org/book/ch02.html#brown-corpus)