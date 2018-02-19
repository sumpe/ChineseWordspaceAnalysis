from wordspace_data_processing import extract_vocab_from_directory, filter_ngrams_only, list_intersection_size
from time import time


def vocab_overlap(wordspace1, wordspace2):
    vocab_1 = extract_vocab_from_directory(wordspace1)
    vocab_2 = extract_vocab_from_directory(wordspace2)
    overlap_size = list_intersection_size(vocab_1, vocab_2)
    return overlap_size


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
    overlap_size = list_intersection_size(vocab_1, vocab_2)
    return overlap_size
