from unittest import TestCase

from src.utils.string_utils import EMPTY_STRING, is_string, has_length


class TestStringUtils(TestCase):

    def test_should_return_true_if_value_is_string(self):
        value = EMPTY_STRING
        self.assertTrue(is_string(value))

    def test_should_return_false_if_value_is_not_string(self):
        value = 3.333
        self.assertFalse(is_string(value))

    def test_should_return_true_if_value_has_length(self):
        value = 'value'
        self.assertTrue(has_length(value))

    def test_should_return_false_if_value_has_no_length(self):
        value = EMPTY_STRING
        self.assertFalse(has_length(value))
