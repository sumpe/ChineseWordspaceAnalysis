from wordspace_data_processing import extract_vocab_from_directory_with_frequency, get_ngrams_of_given_length, get_list_intersection, assert_chinese
from scipy.stats import spearmanr
from time import time


def ngram_frequency_rank_correlation(wordspace1, wordspace2, length):
    vocab1 = extract_vocab_from_directory_with_frequency(wordspace1)
    vocab2 = extract_vocab_from_directory_with_frequency(wordspace2)
    # grams1 = get_ngrams_of_given_length(list(vocab1.keys()), length)
    # grams2 = get_ngrams_of_given_length(list(vocab2.keys()), length)
    grams1 = get_ngrams_of_given_length([key for key in list(vocab1.keys())], length)
    grams2 = get_ngrams_of_given_length([key for key in list(vocab2.keys())], length)
    overlapping_grams = get_list_intersection(grams1, grams2)
    print(len(overlapping_grams), 'overlapping out of', len(grams1)+len(grams2))
    data_points = [(vocab1[word], vocab2[word]) for word in overlapping_grams]
    # vec1 = [vocab1[word] for word in overlapping_grams]
    # vec2 = [vocab2[word] for word in overlapping_grams]
    correlation = spearmanr(data_points)
    return correlation


start = time()
print(ngram_frequency_rank_correlation('just1000/2017-12-12', 'just1000/2018-02-14', 2))

end = time()
print(end - start)
