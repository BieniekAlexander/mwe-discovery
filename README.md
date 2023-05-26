# Introduction
A workspace for the task of mining multiword expressions (MWEs) from a corpus of text.

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