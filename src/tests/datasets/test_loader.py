from unittest import TestCase

from src import load_covid, load_apartments


class TestLoader(TestCase):

    def test_should_load_covid_when_number_of_rows_given(self):
        number_of_rows = 10
        covid = load_covid(number_of_rows)
        self.assertTrue(number_of_rows == len(covid))

    def test_should_load_apartments_when_number_of_rows_given(self):
        number_of_rows = 1
        apartments = load_apartments(number_of_rows)
        self.assertTrue(number_of_rows == len(apartments))
