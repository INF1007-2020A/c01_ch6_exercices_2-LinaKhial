#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
from collections import Counter

import exercice


class TestExercice(unittest.TestCase):
    def test_list_to_dict(self):
        values = [
            ["a", "b", "z", "patate"],
            ["a", "2", "hello", "tigre"]
        ]

        output = [exercice.list_to_dict(v) for v in values]
        answer = [{"a": 0, "b": 1, "z": 2, "patate": 3}, {"a": 0, "2": 1, "hello": 2, "tigre": 3}]

        self.assertListEqual(
            output,
            answer,
            'Mauvaise reponse'
        )

    def test_color_name_to_hex(self):
        colors = [["blue", "red", "green", "yellow", "black", "white"],
                  ["orange", "blue", "red", "brown"]]
        
        answer = [[('blue', '#0000FF'), ('red', '#FF0000'), ('green', '#008000'), ('yellow', '#FFFF00'), ('black', '#000000'), ('white', '#FFFFFF')],
                    [('orange', '#FFA500'), ('blue', '#0000FF'), ('red', '#FF0000'), ('brown', '#A52A2A')]]
        output = [exercice.color_name_to_hex(v) for v in colors]

        self.assertEqual(
            output,
            answer,
            'Mauvaise reponse'
        )

    def test_odd_integer_for_loop(self):
        integer = 46
        output = exercice.odd_integer_for_loop(integer)
        answer = [i for i in range(integer) if i % 2 == 1]

        self.assertEqual(
            output,
            answer,
            'Mauvaise reponse'
        )

    def test_odd_integer_list_comprehension(self):
        integer = 25
        output = exercice.odd_integer_list_comprehension(integer)
        answer = [i for i in range(integer) if i % 2 == 1]

        self.assertEqual(
            output,
            answer,
            'Mauvaise reponse'
        )

    def test_word_dict_for_loop(self):
        words = ["Given", "a", "two", "list", "of", "equal", "size", "create"]
        output = exercice.word_dict_for_loop(words)
        answer = {word[0].upper(): word for word in words}

        self.assertEqual(
            output,
            answer,
            'Mauvaise reponse'
        )

    def test_word_dict_comprehension(self):
        words = ["Given", "a", "two", "list", "of", "equal", "size", "create"]
        output = exercice.word_dict_comprehension(words)
        answer = {word[0].upper(): word for word in words}

        self.assertEqual(
            output,
            answer,
            'Mauvaise reponse'
        )

if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)