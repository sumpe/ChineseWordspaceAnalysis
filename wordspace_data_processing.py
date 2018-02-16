import csv
import os
import re


def extract_vocab(csv_file):
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        return [row['entry'] for row in reader]


def extract_vocab_from_directory(word_space_directory):
    vocab = []
    for file in os.listdir(word_space_directory):
        vocab += extract_vocab(word_space_directory + '/' + file)
    return vocab


def assert_chinese(string):
    """Asserts the presence of a Chinese character in a string. Does not account for if there are other non-Chinese
    characters present."""
    return bool(re.search('[\u4e00-\u9fff]', string))


def assert_gav_chinese(string):
    """Checks in the string is Chinese formatted in Gavagai style (char-space-char). Rejects anything else."""
    return bool(re.match('^[\u4e00-\u9fff]( [\u4e00-\u9fff])*$', string))
