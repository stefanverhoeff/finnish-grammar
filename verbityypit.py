#!/usr/bin/env python3

import re
import sys
from pprint import pprint

# Vowels: https://en.wikibooks.org/wiki/Finnish/Grammar-Vowel_harmony
VOWELS_FRONT = list('yöä')
VOWELS_NEUTRAL = list('ei')
VOWELS_BACK = list('oau')
VOWELS = VOWELS_FRONT + VOWELS_NEUTRAL + VOWELS_BACK
KPT_STRONG_TO_WEAK = [
    ('kk', 'k'),
    ('pp', 'p'),
    ('tt', 't'),
    ('rt', 'rr'),
    ('lt', 'll'),
    ('nt', 'nn'),
    ('nk', 'ng'),
    ('mp', 'mm'),
    ('k', ''),
    ('p', 'v'),
    ('t', 'd'),
]
KPT_WEAK_TO_STRONG = [ (b, a) for a, b in KPT_STRONG_TO_WEAK if b != '']

print('Finnish verbs are fun!')


def verb_has_front_vowel(verb):
    return True in [vowel in verb for vowel in VOWELS_FRONT]


def verb_has_back_vowel(verb):
    return True in [vowel in verb for vowel in VOWELS_BACK]


def verb_type(verb):
    """Return verbityyppi as number or None if not a verb"""
    # Reference: https://thefinnishteacher.weebly.com/verbityypit-ja-preesens--verb-types-and-the-present-tense.html

    if verb[-2] in VOWELS and verb[-1] in VOWELS:
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


def verb_root(verb):
    "Root of verb (vartalo), without KPT applied"
    verbityypi = verb_type(verb)

    if verbityypi == 1:
        return verb[:-1]
    if verbityypi == 2:
        return verb[:-2]
    if verbityypi == 3:
        return verb[:-2] + 'e'
    if verbityypi == 4:
        return verb[:-2] + verb[-1]
    if verbityypi == 5:
        return verb[:-1] + 'se'
    if verbityypi == 6:
        return verb[:-2] + 'ne'

    return None


def kpt_strong_to_weak(word):
    return transform_word_with(word, KPT_STRONG_TO_WEAK)


def kpt_weak_to_strong(word):
    return transform_word_with(word, KPT_WEAK_TO_STRONG)


def transform_word_with(word, transformations):
    assert len(word) > 1, "word should be at least 2 chars long"
    assert not re.search(r'[A-Z]+', word), f"only lowercase chars expected, found capitals in '{word}'"

    # Don't transform first+last character
    first_char = word[0]
    last_char = word[-1]
    middle = word[1:-1]

    for search, replacement in transformations:
        if search in middle:
            middle = middle.replace(search, replacement)
            # FIXME: Only do wrong transformation per word, probably wrong assumption
            # Need more sophisticated algorythm
            break

    return first_char + middle + last_char


def pronoun_suffix(verb, pronoun):
    verbityypi = verb_type(verb)

    if pronoun == 'minä':
        return 'n'
    if pronoun == 'sinä':
        return 't'
    if pronoun == 'hän' and verbityypi == 2:
        return ''
    if pronoun == 'hän' and verbityypi != 2:
        return verb_root(verb)[-1]
    if pronoun == 'me':
        return 'mme'
    if pronoun == 'te':
        return 'tte'
    # TODO: handle compound words (is that common for verbs?)
    if pronoun == 'he' and verb_has_back_vowel(verb):
        return 'vat'
    if pronoun == 'he' and not verb_has_back_vowel(verb):
        return 'vät'

    return None


def conjugate_verb_tyyppi1(verb, pronoun):
    root = verb_root(verb)
    suffix = pronoun_suffix(verb, pronoun)

    if pronoun != 'hän' and pronoun != 'he':
        root = kpt_strong_to_weak(root)

    conjugated_verb = root + suffix

    return conjugated_verb


def main():
    verb = 'olla'
    if len(sys.argv) > 1:
        verb = sys.argv[1].lower().strip()

    verb_type = verb_type(verb)
    print('The verbityyppi for {} is {}'.format(
        verb, verb_type))


if __name__ == '__main__':
    main()
