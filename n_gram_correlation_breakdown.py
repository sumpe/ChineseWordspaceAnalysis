from wordspace_data_processing import extract_vocab, get_ngrams_of_given_length
from scipy.stats import spearmanr


def ngram_frequency_rank_correlation(wordspace1, wordspace2, length):
    #vocab1 = extract_vocab(wordspace1)
    #vocab2 = extract_vocab(wordspace2)
    #vocab1 = get_ngrams_of_given_length(vocab1, length)
    #vocab2 = get_ngrams_of_given_length(vocab2, length)
    correlation = spearmanr(vocab1, vocab2)
    return correlation

print(ngram_frequency_rank_correlation('top20wordspaces/2017-12-12','top20wordspaces/2018-02-14'))
