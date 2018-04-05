import argparse
import re

from collections import Counter


def load_data(filepath):
    with open(filepath, 'r') as text_file:
        content = text_file.read()
    return content


def tokenize_text(text_string):
    words_list = re.split(r'(?:\W|\s)\s*', text_string)
    return filter(bool, words_list)


def get_most_frequent_words(text_string, top=30):
    counter = Counter(text_string)
    return counter.most_common(top)


def print_top_words(words_list):
    row_format = '{:<10} | {:>10}'

    print('Top {} most common words '
          'in the file:\n'.format(len(words_list)))
    print(row_format.format('Word', 'Occurrences'))
    print('-' * 23)
    for word, occurrences in words_list:
        print(row_format.format(word, occurrences))


def get_args():
    parser = argparse.ArgumentParser(
        description='Word frequency analyzer'
    )

    parser.add_argument(
        '-f', '--filepath',
        help='path to txt file',
        required=True
    )
    return parser.parse_args()


if __name__ == '__main__':

    args = get_args()

    loaded_text = load_data(args.filepath)

    tokenized_data = tokenize_text(loaded_text)

    top_words = get_most_frequent_words(tokenized_data)

    print_top_words(top_words)
