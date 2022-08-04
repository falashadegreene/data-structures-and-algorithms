
from data_structures.stack import Stack


def multi_bracket_validation(string):
    brackets = Stack()
    brackets_dictionary = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in string:
        if char == '[' or char == '{' or char == '(':
            brackets.push(char)
        if brackets_dictionary.get(char):
            if not brackets.peek():
                return False
            pop = brackets.pop()
            if brackets_dictionary(char) != pop:
                return False
    if not brackets.is_empty():
        return False
    return True
