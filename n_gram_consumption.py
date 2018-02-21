from wordspace_data_processing import extract_vocab_from_directory, list_intersection_size
from time import time


def compare_bad_space_with_good_space(good_space, bad_space):
    good_vocabulary = extract_vocab_from_directory(good_space)
    bad_vocabulary = extract_vocab_from_directory(bad_space)
    total = len(good_vocabulary)
    overlapping = list_intersection_size(good_vocabulary, bad_vocabulary)
    new_words = [word for word in bad_vocabulary if word not in good_vocabulary]
    dropped_out_words = [word for word in good_vocabulary if word not in bad_vocabulary]
    print(len(dropped_out_words))
    print('start to count')
    count = 0
    for dropped_word in dropped_out_words:
        for new_word in new_words:
            if dropped_word in new_word:
                count += 1
                break
    print(overlapping, overlapping/total)
    print(count, count/len(dropped_out_words))


start = time()
compare_bad_space_with_good_space('lexicon/2017-12-12', 'lexicon/2018-02-14')
end = time()

print(end-start)
