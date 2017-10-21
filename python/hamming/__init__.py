# -*- coding: utf-8 -*-

# Copyright (c) 2017 My Employer, All rights reserved.
# Author: Martin Koistinen


def compute(string_a, string_b):
    """
    Computes the Hamming-distance for two given DNA-strings of identical length

    :param string_a: String of base-pairs in CGAT notation
    :param string_b: String of base-pairs in CGAT notation
    :return: Returns the Hamming distance of the two strings
    """

    # Ensure strings are same length of less than 1kbp.
    length = len(string_a)
    if length != len(string_b):
        raise ValueError('Input strings must contain the same number of '
                         'base-pairs.')

    # NOTE: The provided reference link to Rosalind suggests that the given
    # two strings will not exceed 1kbp. However, I did not find this to be
    # a theoretical restriction of any sort in my brief research, so, I assume
    # this is merely a note to test-takers about the size they should plan for
    # and not a test requirement. Otherwise, I would just issue a warning when
    # `length` exceeds 1000.

    # NOTE: The "reference" Python implementation for the Hamming distance at
    # https://en.wikipedia.org/wiki/Hamming_distance is unnecessarily "clever"
    # using:
    #
    #    return sum(el1 != el2 for el1, el2 in zip(string_a, string_b))
    #
    # This is about 1/2 as fast as the more readable implementation below on
    # Python 2.7. The following is still faster on Python 3.6.

    distance = 0
    for position in range(length):
        if string_a[position] != string_b[position]:
            distance += 1

    return distance
