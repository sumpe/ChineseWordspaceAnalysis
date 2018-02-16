import os
from nltk import FreqDist
import matplotlib.pyplot as plt
from wordspace_data_processing import extract_vocab, assert_gav_chinese


def list_words_to_list_word_lengths(word_list):
    return [len(word.split()) for word in word_list if assert_gav_chinese(word)]


def n_gram_length_freq_dist(word_space_directory):
    word_space_vocab = []
    for redis_dump in os.listdir(word_space_directory):
        file_vocab = extract_vocab(word_space_directory + '/' + redis_dump)
        word_space_vocab += file_vocab
    word_length_list = list_words_to_list_word_lengths(word_space_vocab)
    length_freq_dist = FreqDist(word_length_list)
    return (word_space_directory, sorted(length_freq_dist.most_common()))


def plot_freq_dists(list_of_sorted_freq_dists):
    total = len(list_of_sorted_freq_dists)
    shift = 1/total
    width = 0.8 * shift
    count = 0
    plt.clf()
    plt.title('Plot of n-gram composition in word space')
    plt.xlabel('N-gram length')
    plt.ylabel('Occurrence')
    labels = []
    for title, freq_dist in list_of_sorted_freq_dists:
        grams = [gram + shift * count - 0.5 * shift for gram, _ in freq_dist][4:]
        bars = [occurrence for _, occurrence in freq_dist][4:]
        plt.bar(grams, bars, width=width)
        labels.append(title)
        count += 1
    plt.legend(labels)
    plt.show()


def compare_spaces(directory_of_wordspaces):
    data = []
    for word_space in os.listdir(directory_of_wordspaces):
        titled_freq_dist = n_gram_length_freq_dist(directory_of_wordspaces + '/' + word_space)
        _, n_gram_length_data = titled_freq_dist
        print(n_gram_length_data)
        data.append(titled_freq_dist)
    plot_freq_dists(data)


def n_grams_in_vocabulary(directory_of_wordspaces):
    for wordspace in os.listdir(directory_of_wordspaces):
        titled_freq_dist = n_gram_length_freq_dist(directory_of_wordspaces + '/' + wordspace)
        title, data = titled_freq_dist
        ngramstotal = sum(occ for gram, occ in data if gram > 1)
        print(title, 'there are', ngramstotal, 'ngrams')


# for term in extract_vocab('wordspaces/2017-12-12/redis-keys-zh-prod-1.csv'):
#     print(assert_gav_chinese(term), term, len(term), term.split(), len(term.split()))
# compare_spaces('top20wordspaces')

n_grams_in_vocabulary('wordspaces')
