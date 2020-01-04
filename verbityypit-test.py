#!/usr/bin/env python3

import unittest
import verbityypit


class TestVeritTyypit(unittest.TestCase):

    def test_verb_types(self):
        verbs = {
            'puhua':        1, # speak (1)
            'kirjoittaa':   1, # write (1)
            'lukea':        1, # read (1)
            'ymmärtää':     1, # understand (1)

            'syödä':        2, # eat (2)
            'juoda':        2, # drink (2)
            'viedä':        2, # take, get (2)
            'imuroida':     2, # vacuum (2)

            'ajatella':     3, # think (3)
            'purra':        3, # byte (3)
            'mennä':        3, # go (3)
            'pestä':        3, # wash (3)

            'haluta':       4, # want (4)
            'tavata':       4, # meet (4)
            'osata':        4, # know (4)
            'pudota':       4, # drop (4)

            'valita':       5, # choose (5)
            'tarvita':      5, # need (5)
            'mainita':      5, # mention (5)
            'häiritä':      5, # disturb (5)

            'paeta':        6, # escape (6)
            'vanheta':      6, # grow old (6)
            'kyetä':        6, # be able to (6)
            'pidetä':       6, # lengthen (6)
        }

        for verb in verbs.keys():
            verb_type = verbityypit.verb_type(verb)
            print('The verbityyppi for {} is {}'.format(
                verb, verb_type))

            self.assertEqual(verbs[verb], verb_type)

    def test_verb_root(self):
        self.assertEqual('puhu', verbityypit.verb_root('puhua'))
        self.assertEqual('vie', verbityypit.verb_root('viedä'))
        self.assertEqual('mene', verbityypit.verb_root('mennä'))
        self.assertEqual('halua', verbityypit.verb_root('haluta'))
        self.assertEqual('valitse', verbityypit.verb_root('valita'))
        self.assertEqual('venhene', verbityypit.verb_root('venheta'))

    # def test_verb_root_kpt_strong_to_weak(self):
    #     # TODO
    #     self.assertEqual('puhu', verbityypit.verb_root('puhua'))
    #     self.assertEqual('vie', verbityypit.verb_root('viedä'))
    #     self.assertEqual('men', verbityypit.verb_root('mennä'))
    #     self.assertEqual('puhu', verbityypit.verb_root('puhua'))
    #     self.assertEqual('puhu', verbityypit.verb_root('puhua'))
    #     self.assertEqual('puhu', verbityypit.verb_root('puhua'))

    def test_kpt_strong_to_weak(self):
        self.assertEqual('panki', verbityypit.kpt_strong_to_weak('pankki'))
        self.assertEqual('kaupa', verbityypit.kpt_strong_to_weak('kauppa'))
        self.assertEqual('kato', verbityypit.kpt_strong_to_weak('katto'))
        self.assertEqual('joi', verbityypit.kpt_strong_to_weak('joki'))
        self.assertEqual('halva', verbityypit.kpt_strong_to_weak('halpa'))
        self.assertEqual('pöydä', verbityypit.kpt_strong_to_weak('pöytä'))
        self.assertEqual('parra', verbityypit.kpt_strong_to_weak('parta'))
        self.assertEqual('silla', verbityypit.kpt_strong_to_weak('silta'))
        self.assertEqual('ranna', verbityypit.kpt_strong_to_weak('ranta'))
        self.assertEqual('Helsingi', verbityypit.kpt_strong_to_weak('Helsinki'))
        self.assertEqual('kamma', verbityypit.kpt_strong_to_weak('kampa'))

    # TODO KPT Edge cases:
    # don't match beginning/end of word
    # multiple matches of same transformation in a string
    # multiple different transformations in a string
    # do kk, pp, tt etc before k, p, t
    # compound words, only KPT is some parts?

    # TODO: KPT weak to strong


    def test_pronoun_suffix_basic_cases(self):
        verb = 'puhua'
        self.assertEqual('n', verbityypit.pronoun_suffix(verb, 'minä'))
        self.assertEqual('t', verbityypit.pronoun_suffix(verb, 'sinä'))
        self.assertEqual('u', verbityypit.pronoun_suffix(verb, 'hän'))
        self.assertEqual('mme', verbityypit.pronoun_suffix(verb, 'me'))
        self.assertEqual('tte', verbityypit.pronoun_suffix(verb, 'te'))
        self.assertEqual('vat', verbityypit.pronoun_suffix(verb, 'he'))

    def test_pronoun_suffix_special_cases(self):
        verb = 'käydä'
        self.assertEqual('n', verbityypit.pronoun_suffix(verb, 'minä'))
        self.assertEqual('t', verbityypit.pronoun_suffix(verb, 'sinä'))
        self.assertEqual('', verbityypit.pronoun_suffix(verb, 'hän'))
        self.assertEqual('mme', verbityypit.pronoun_suffix(verb, 'me'))
        self.assertEqual('tte', verbityypit.pronoun_suffix(verb, 'te'))
        self.assertEqual('vät', verbityypit.pronoun_suffix(verb, 'he'))

    def test_verb_has_front_vowel(self):
        self.assertTrue(verbityypit.verb_has_front_vowel('käydä'))
        self.assertTrue(verbityypit.verb_has_front_vowel('ymmärtää'))
        self.assertTrue(verbityypit.verb_has_front_vowel('käyttää'))
        self.assertFalse(verbityypit.verb_has_front_vowel('olla'))
        self.assertFalse(verbityypit.verb_has_front_vowel('muistaa'))
        self.assertFalse(verbityypit.verb_has_front_vowel('katsoa'))

    def test_verb_has_back_vowel(self):
        self.assertTrue(verbityypit.verb_has_back_vowel('soittaa'))
        self.assertTrue(verbityypit.verb_has_back_vowel('harjata'))
        self.assertTrue(verbityypit.verb_has_back_vowel('puhua'))
        self.assertFalse(verbityypit.verb_has_back_vowel('nähdä'))
        self.assertFalse(verbityypit.verb_has_back_vowel('etsiä'))
        self.assertFalse(verbityypit.verb_has_back_vowel('tehdä'))

# TODO
    # def test_conjugate_verb_tyyppi1(self):
    #     self.assertEqual('puhun', verbityypit.conjugate_verb_tyyppi1('puhua', 'minä'))
    #     self.assertEqual('puhut', verbityypit.conjugate_verb_tyyppi1('puhua', 'sinä'))
    #     self.assertEqual('puhuu', verbityypit.conjugate_verb_tyyppi1('puhua', 'hän'))
    #     self.assertEqual('puhumme', verbityypit.conjugate_verb_tyyppi1('puhua', 'me'))
    #     self.assertEqual('puhutte', verbityypit.conjugate_verb_tyyppi1('puhua', 'te'))
    #     self.assertEqual('puhuvat', verbityypit.conjugate_verb_tyyppi1('puhua', 'he'))

if __name__ == '__main__':
    unittest.main()
