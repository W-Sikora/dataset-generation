from .datasets import load_apartments, load_covid
from .generators.problems import generate_classification_problem, generate_regression_problem
from .generators.features import generate_categorical_features
from .requirements import check_requirements, get_recommended_versions

__all__ = [
    'check_requirements',
    'get_recommended_versions',
    'load_apartments',
    'load_covid',
    'generate_classification_problem',
    'generate_regression_problem',
    'generate_categorical_features',
]
