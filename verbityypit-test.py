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
            verb_type = verbityypit.find_verb_type(verb)
            print('The verbityyppi for {} is {}'.format(
                verb, verb_type))

            self.assertEqual(verbs[verb], verb_type)


if __name__ == '__main__':
    unittest.main()
