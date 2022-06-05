from unittest import TestCase

from src.utils.assertions import not_none, is_true, has_length, is_valid_probability, contains_x_elements
from src.utils.string_utils import EMPTY_STRING


class TestAssertions(TestCase):

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

    def test_should_raise_value_error_when_probability_is_greater_than_one(self):
        incorrect_probability_value = 1.01
        self.assertRaises(ValueError, is_valid_probability, incorrect_probability_value)

    def test_should_raise_value_error_when_probability_is_less_than_zero(self):
        incorrect_probability_value = - 0.01
        self.assertRaises(ValueError, is_valid_probability, incorrect_probability_value)

    def test_should_raise_value_error_when_container_does_not_contain_indicated_number_of_elements(self):
        container = [1, 2]
        indicated_number_of_elements = 0
        self.assertRaises(ValueError, contains_x_elements, container, indicated_number_of_elements)