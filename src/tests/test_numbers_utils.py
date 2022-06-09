from unittest import TestCase

from src.utils.numbers_utils import is_between_inclusive


class TestNumbersUtils(TestCase):

    def test_should_return_true_if_value_is_in_range(self):
        minimum, maximum = -2.1, 2.1
        value = 0.333
        self.assertTrue(is_between_inclusive(value, minimum, maximum))

    def test_should_return_false_if_value_is_in_range(self):
        minimum, maximum = 1.1, 2.1
        value = 3.333
        self.assertFalse(is_between_inclusive(value, minimum, maximum))
