from unittest import TestCase

from utils.assertions import has_length, not_none, is_true
from utils.string_utils import EMPTY_STRING


class TestAssertion(TestCase):

    def test_should_raise_value_error_when_value_is_none(self):
        value = None
        self.assertRaises(ValueError, not_none, value)

    def test_should_raise_value_error_when_string_value_is_none(self):
        value = None
        self.assertRaises(ValueError, has_length, value)

    def test_should_raise_value_error_when_string_value_is_empty(self):
        value = EMPTY_STRING
        self.assertRaises(ValueError, has_length, value)

    def test_should_raise_value_error_when_condition_is_false(self):
        condition = False
        self.assertRaises(ValueError, is_true, condition)
