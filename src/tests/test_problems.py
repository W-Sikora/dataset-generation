from unittest import TestCase
from pandas import DataFrame
import numpy.random as rnd

from src import generate_regression_problem


class TestProblems(TestCase):

    @staticmethod
    def form_features():
        return DataFrame({
            'x1': rnd.uniform(1, 10, 10),
            'x2': rnd.uniform(-3, 3, 10)
        })

    @staticmethod
    def form_target_function():
        return 'z = x1 * -2 * x2'

    @staticmethod
    def form_output_name():
        return 'y'

    def test_should_change_output_name(self):
        features = TestProblems.form_features()
        target_function = TestProblems.form_target_function()
        output_name = TestProblems.form_target_function()

        inputs, outputs = generate_regression_problem(features, target_function, output_name)

        self.assertEqual(outputs.name, output_name)
