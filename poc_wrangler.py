"""
Student code for Word Wrangler game
"""

# import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """

    if len(list1) == 0:
        return list1

    result = []
    for each_item in list1:
        if each_item not in result:
            result.append(each_item)

    return result


def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    result = []

    for each_item in list1:
        if each_item in list2:
            result.append(each_item)

    return result


# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """
    result = []

    index1 = 0
    index2 = 0

    while index1 < len(list1) and index2 < len(list2):
        # both lists still have items
        if list1[index1] < list2[index2]:
            result.append(list1[index1])
            index1 += 1
        else:
            result.append(list2[index2])
            index2 += 1

    if index1 < len(list1):
        # list1 still have items left, which means all list2 items are smaller and already in result
        for sec_index1 in range(index1, len(list1)):
            result.append(list1[sec_index1])

    if index2 < len(list2):
        # list2 still have items left, which means all list1 items are smaller and already in result
        for sec_index2 in range(index2, len(list2)):
            result.append(list2[sec_index2])

    return result


def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    result = list1
    if len(result) < 2:
        return result

    first_half = result[0:len(result) / 2]
    second_half = result[len(result) / 2:]

    result = merge(merge_sort(first_half), merge_sort(second_half))
    return result

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    return []


# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []


def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()




