from unittest import TestCase

from utils.signs import Sign


class TestSign(TestCase):

    def test_is_division(self):
        sign = '/'
        is_division = Sign.is_division(sign)
        self.assertTrue(is_division)

    def test_is_minus(self):
        sign = '-'
        is_minus = Sign.is_minus(sign)
        self.assertTrue(is_minus)

    def test_is_plus(self):
        sign = '+'
        is_plus = Sign.is_plus(sign)
        self.assertTrue(is_plus)

    def test_is_power(self):
        sign = '**'
        is_power = Sign.is_power(sign)
        self.assertTrue(is_power)

    def test_is_times(self):
        sign = '*'
        is_times = Sign.is_times(sign)
        self.assertTrue(is_times)

    def test_basic(self):
        basic_signs = {
            Sign.DIVISION,
            Sign.MINUS,
            Sign.PLUS,
            Sign.TIMES
        }
        self.assertSetEqual(basic_signs, Sign.basic())

    def test_positive_and_negative(self):
        positive_and_negative_signs = {
            Sign.MINUS,
            Sign.PLUS
        }
        self.assertSetEqual(positive_and_negative_signs, Sign.positive_and_negative())
