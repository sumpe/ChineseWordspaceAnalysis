from wordspace_data_processing import extract_vocab_from_directory, list_intersection_size
from time import time


def compare_bad_space_with_good_space(good_space, bad_space):
    good_vocabulary = extract_vocab_from_directory(good_space)
    bad_vocabulary = extract_vocab_from_directory(bad_space)
    previous_full_space = extract_vocab_from_directory('wordspaces/2017-12-12')
    total = len(good_vocabulary)
    overlapping = list_intersection_size(good_vocabulary, bad_vocabulary)
    new_words = [word for word in bad_vocabulary if word not in good_vocabulary]
    print('start to count')
    count = 0
    for good_word in good_vocabulary:
        for new_word in new_words:
            if new_word not in previous_full_space:
                if good_word in new_word:
                    count += 1
                    break
    print(overlapping, overlapping/total)
    print(count, count/total)


start = time()
compare_bad_space_with_good_space('lexicon/2017-12-12', 'wordspaces/2018-02-14')
end = time()

print(end-start)
