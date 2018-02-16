from wordspace_data_processing import extract_vocab_from_directory, assert_chinese


def measure_non_chinese_vocab_items(wordspace):
    vocabulary = extract_vocab_from_directory(wordspace)
    total = len(vocabulary)
    chinese = sum(1 for word in vocabulary if assert_chinese(word))
    non_chinese = total - chinese
    print('Wordspace:', wordspace[-10:])
    print('Total:', '\t\t\t', total)
    print('Chinese:', '\t\t', chinese, '\t', str(100*round(chinese/total, 4)) + '%')
    print('Non Chinese:', '\t', non_chinese, '\t', str(100*round(non_chinese/total, 4)) + '%')
    print()


measure_non_chinese_vocab_items('wordspaces/2017-12-12')
measure_non_chinese_vocab_items('wordspaces/2018-02-14')
measure_non_chinese_vocab_items('top20wordspaces/2017-12-12')
measure_non_chinese_vocab_items('top20wordspaces/2018-02-14')
