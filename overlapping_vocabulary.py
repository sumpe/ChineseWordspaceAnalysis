from wordspace_data_processing import extract_vocab_from_directory
from time import time


def all_vocab_overlap(wordspace1, wordspace2):
    vocab_1 = extract_vocab_from_directory(wordspace1)
    vocab_2 = extract_vocab_from_directory(wordspace2)
    concatenation = vocab_1 + vocab_2
    size_with_duplicates = len(concatenation)
    concatenation = set(concatenation)
    size_without_duplicates = len(concatenation)
    intersection_size = size_with_duplicates - size_without_duplicates
    return intersection_size


start = time()
print(all_vocab_overlap('top20wordspaces/2017-12-12', 'top20wordspaces/2018-02-14'))
print(all_vocab_overlap('wordspaces/2017-12-12', 'wordspaces/2018-02-14'))
end = time()
print('Running Time', end-start)