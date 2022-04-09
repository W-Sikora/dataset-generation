from unittest import TestCase
from generators.expressions_generator import generate_sign
from utils.signs import Sign


class TestAssertion(TestCase):

    def test_should_generate_sign(self):
        sign = generate_sign()
        self.assertTrue(sign in Sign.positive_and_negative())

    def test_generate_coefficient(self):
        pass

    def test_generate_single_term(self):
        pass