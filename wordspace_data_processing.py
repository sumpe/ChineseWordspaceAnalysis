import csv
import os


def extract_vocab(csv_file):
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        return [row['entry'] for row in reader]


def extract_vocab_from_directory(word_space_directory):
    vocab = []
    for file in os.listdir(word_space_directory):
        vocab += extract_vocab(word_space_directory + ' ' + file)
    return vocab
