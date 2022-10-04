from data_structures.hashtable import Hashtable
import re


def first_repeated_word(string):
    regex = re.compile('[^a-zA-Z ]')
    stripped = regex.sub('', string)
    words = stripped.lower().split()
    dict = set()

    for string in words:
        if string in dict:
            return string
        else:
            dict.add(string)


