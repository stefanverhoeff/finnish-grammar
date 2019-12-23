#!/usr/bin/env python3

import sys
from pprint import pprint

print('Finnish verbs are fun!')


def find_verb_type(verb):
    """return verbityyppi as number or None if not a verb"""
    # Reference: https://thefinnishteacher.weebly.com/verbityypit-ja-preesens--verb-types-and-the-present-tense.html
    vowels = list('eyuioaöä')

    if verb[-2] in vowels and verb[-1] in vowels:
        return 1
    if verb[-2:] in ['da', 'dä']:
        return 2
    if verb[-2:] in ['la', 'ra', 'na', 'lä', 'rä', 'nä'] or verb[-3:] in ['sta', 'stä']:
        return 3
    if verb[-3:] in ['ita', 'itä']:
        return 5
    if verb[-3:] in ['eta', 'etä']:
        return 6
    if verb[-2:] in ['ta', 'tä']:
        return 4

    return None


def main():
    verb = 'olla'
    if len(sys.argv) > 1:
        verb = sys.argv[1].lower().strip()

    verb_type = find_verb_type(verb)
    print('The verbityyppi for {} is {}'.format(
        verb, verb_type))


if __name__ == '__main__':
    main()
