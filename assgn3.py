"""
References taken from :
#https://stackoverflow.com/questions/29317937/how-can-i-capitalize-a-character-with-an-odd-numbered-index-in-a-string
#https://stackoverflow.com/questions/40698769/reversing-words-in-a-python-string-including-punctuation
#https://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python
#https://stackoverflow.com/questions/1277914/is-there-a-way-to-output-the-numbers-only-from-a-python-list
"""

import string

def alternate_case(s: str, upper_first=True) -> str:
    """Given an arbitrary string, convert every odd character to
    upper case and even to lower-case (or vice-versa)
    :param s: a string to start with
    :param upper_first: defaults to uppers first, set False for opposite
    :return: the altered string
    >>> alternate_case('abcdefg')
    'AbCdEfG'
    >>> alternate_case('abcdefg', upper_first=False)
    'aBcDeFg'
    >>> alternate_case('The Three-Body Problem, by Cixin Liu')
    'ThE ThReE-BoDy pRoBlEm, By cIxIn lIu'
    """
    word2 = ""
    if upper_first == True:
        for i, v in enumerate(s):
            if i % 2 == 0:
                word2 += v.upper()
            else:
                word2 += v.lower()
    elif upper_first == False:
        for i, v in enumerate(s):
            if i % 2 != 0:
                word2 += v.upper()
            else:
                word2 += v.lower()
    #print(word2)
    return word2


def get_every_number(mixed_list: list) -> list:
    """Create a new list from a mixed-type list, keeping only the number type items.
    In other words, it ignores strings, tuples, sublists, dictionaries, etc.
    :param mixed_list: a 1-dimensional list containing various types of data
    :return: a new list containing only the items that are number types
    >>> get_every_number(['abc', 42, 3.14159, 2 * 4, '9'])
    [42, 3.14159, 8]
    >>> get_every_number([75, 101010101, 0xC0ffee, 'java'])
    [75, 101010101, 12648430]
    """
    mixed_list = [e for e in mixed_list if isinstance(e, (int, float))]
    #print(mixed_list)
    return mixed_list


def back_words(s: str) -> str:
    """Rearrange a string so that every word gets spelled backwards but the
    sequence of words and any punctuation stays the same.
    :param s: any string
    :return: a string with words in the same order but each word spelled backwards.
    >>> back_words('even yellow apples are not bananas.')
    'neve wolley selppa era ton sananab.'
    >>> back_words('to be or not to be, that is the question.')
    'ot eb ro ton ot eb, taht si eht noitseuq.'
    """
    punctuation = set(string.punctuation)
    words = []
    for word in s.split():
        words.append(word.rstrip(string.punctuation)[::-1])
        if word[-1] in punctuation:
            words[-1] = words[-1] + word[-1]
    str1 = ' '.join(words)
    #print(str1)
    return str1


def flatten_list(nested_list: list) -> list:
    """Given a list contains other lists nested to any depth,
    compute a new 1-dimensional list containing all the original non-list
    values in the same order. Non-list collections are kept as-is, not flattened,
    even if they contain other lists.
    :param nested_list: A list that contains other lists, to any depth.
    :return: a 1-dimensional list with all the original non-list values in the same order.
    >>> flatten_list([[[[[1, 2], 3]], 4, 5], 6])
    [1, 2, 3, 4, 5, 6]
    >>> flatten_list(['abc', 2, ['x', 'y'], ['a', 'b'], [[[[[[[[[[['z']]]]]]]]]]]])
    ['abc', 2, 'x', 'y', 'a', 'b', 'z']
    >>> flatten_list([1, 2, (3, [4, 5]), ['cat', 'in', 'the', 'hat']])
    [1, 2, (3, [4, 5]), 'cat', 'in', 'the', 'hat']
    >>> flatten_list(['this list', 'is', 'not', 'nested'])
    Traceback (most recent call last):
    ...
    ValueError: nested_list parameter was already 1-dimensional.
    """
    if any(isinstance(el, list) for el in nested_list) == False:
        raise ValueError('nested_list parameter was already 1-dimensional.')
    else:
        l2 = list(flatten(nested_list))
        #print(l2)
    return l2


def flatten(items):
    if items == []:
        return []
    elif type(items) is not list:
        return [items]
    else:
        return flatten(items[0]) + flatten(items[1:])


def flatten_list1(nested_list1: list) -> list:
    """Given a list contains other lists nested to any depth,
    compute a new 1-dimensional list containing all the original non-list
    values in the same order. Non-list collections are kept as-is, not flattened,
    even if they contain other lists.
    :param nested_list: A list that contains other lists, to any depth.
    :return: a 1-dimensional list with all the original non-list values in the same order.
    """
    if any(isinstance(el, list) for el in nested_list1) == False:
        #print(nested_list)
        return nested_list1
    else:
        l2 = list(flatten(nested_list1))
        #print(l2)
        return l2

def sum_list_numbers(x: list) -> float:
    """Given any list of mixed data types, possibly nested with other lists,
    compute the arithmetic sum of all the numeric values contained in it.
    Supports integers, floats, decimals, and lists thereof. Ignores values
    contained in non-list collections.
    :param x: a list of mixed data types, possibly nested with other lists.
    :return: the sum of all numeric values contained in list x.
    >>> sum_list_numbers([5, 2, 3])
    10.0
    >>> sum_list_numbers([[[2, 5], 4]])
    11.0
    >>> sum_list_numbers([['number 5', [[25.2]]], 0.9, 'x', [4]])
    30.1
    >>> sum_list_numbers([34, 2, (5, 1)])
    36.0
    >>> sum_list_numbers([{45: 5, 100: -200}])
    0.0
    """
    l4 = flatten_list1(x)
    l5 = get_every_number(l4)
    l6 = list(map(float, l5))
    if not l6:
        print(float(sum(l6)))
        #return l6
    else:
        l7 = round(sum(l6),1)
        #print(type(l7))
        #print(l7)
        return l7