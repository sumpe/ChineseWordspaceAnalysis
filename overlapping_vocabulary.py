from wordspace_data_processing import extract_vocab_from_directory, filter_ngrams_only
from time import time


def vocab_overlap(wordspace1, wordspace2):
    vocab_1 = extract_vocab_from_directory(wordspace1)
    vocab_2 = extract_vocab_from_directory(wordspace2)
    concatenation = vocab_1 + vocab_2
    size_with_duplicates = len(concatenation)
    concatenation = set(concatenation)
    size_without_duplicates = len(concatenation)
    intersection_size = size_with_duplicates - size_without_duplicates
    return intersection_size


def ngram_overlap(wordspace1, wordspace2):
    vocab_1 = extract_vocab_from_directory(wordspace1)
    print(wordspace1)
    print('Vocab size:', len(vocab_1))
    vocab_1 = filter_ngrams_only(vocab_1)
    print('N-gram size:', len(vocab_1))
    print(wordspace2)
    vocab_2 = extract_vocab_from_directory(wordspace2)
    print('Vocab size:', len(vocab_2))
    vocab_2 = filter_ngrams_only(vocab_2)
    print('N-gram size:', len(vocab_2))
    concatenation = vocab_1 + vocab_2
    size_with_duplicates = len(concatenation)
    concatenation = set(concatenation)
    size_without_duplicates = len(concatenation)
    intersection_size = size_with_duplicates - size_without_duplicates
    return intersection_size
