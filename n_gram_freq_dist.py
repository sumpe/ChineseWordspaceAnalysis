import csv
import os
from nltk import FreqDist
import matplotlib.pyplot as plt
import re


def extract_vocab(csv_file):
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        return [row['entry'] for row in reader]


def list_words_to_list_word_lengths(word_list):
    return [len(word.split()) for word in word_list if assert_gav_chinese(word)]


def n_gram_length_freq_dist(word_space_directory):
    word_space_vocab = []
    for redis_dump in os.listdir(word_space_directory):
        file_vocab = extract_vocab(word_space_directory + '/' + redis_dump)
        word_space_vocab += file_vocab
    word_length_list = list_words_to_list_word_lengths(word_space_vocab)
    length_freq_dist = FreqDist(word_length_list)
    return sorted(length_freq_dist.most_common(15))


def compare_spaces(directory_of_wordspaces):
    plt.clf()
    for word_space in os.listdir(directory_of_wordspaces):
        n_gram_length_data = n_gram_length_freq_dist(directory_of_wordspaces + '/' + word_space)
        plt.plot(n_gram_length_data)
    plt.show()


def assert_chinese(string):
    """Asserts the presence of a Chinese character in a string. Does not account for if there are other non-Chinese
    characters present."""
    return bool(re.search('[\u4e00-\u9fff]', string))


def assert_gav_chinese(string):
    """Checks in the string is Chinese formatted in Gavagai style (char space char). Rejects anything else."""
    return bool(re.match('^[\u4e00-\u9fff]( [\u4e00-\u9fff])*$', string))


compare_spaces('wordspaces')

# for term in extract_vocab('wordspaces/2017-12-12-morning/redis-keys-zh-prod-1.csv'):
#     print(assert_gav_chinese(term), term, len(term), term.split(), len(term.split()))

# print(n_gram_length_freq_dist('wordspaces/2018-02-14'))
# print(n_gram_length_freq_dist('wordspaces/2017-12-12-morning'))