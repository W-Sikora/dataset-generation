import sys
import src.utils.assertions as assertions
from src.utils.string_utils import DOT

try:
    import pandas as pd
except ImportError:
    pass

try:
    import numpy as np
except ImportError:
    pass

try:
    import scipy as sp
except ImportError:
    pass

try:
    import matplotlib as mp
except ImportError:
    pass

try:
    import seaborn as sn
except ImportError:
    pass

try:
    import fitter as ft
except ImportError:
    pass

try:
    import sklearn as sa
except ImportError:
    pass

PYTHON_VERSION = '3.7.7'
PANDAS_VERSION = '1.2.3'
NUMPY_VERSION = '1.19.5'
MATPLOTLIB_VERSION = '3.3.3'
SEABORN_VERSION = '0.11.2'
FITTER_VERSION = '1.4.0'
SCIPY_VERSION = '1.7.3'
SKLEARN_VERSION = '1.0.2'


def is_python_version_acceptable():
    return __is_version_acceptable(sys.version, PYTHON_VERSION)


def is_pandas_version_acceptable():
    return __is_version_acceptable(pd.__version__, PANDAS_VERSION)


def is_numpy_version_acceptable():
    return __is_version_acceptable(np.__version__, NUMPY_VERSION)


def is_matplotlib_version_acceptable():
    return __is_version_acceptable(mp.__version__, MATPLOTLIB_VERSION)


def is_seaborn_version_acceptable():
    return __is_version_acceptable(sn.__version__, SEABORN_VERSION)


def is_fitter_version_acceptable():
    return __is_version_acceptable(ft.version, FITTER_VERSION)


def is_scipy_version_acceptable():
    return __is_version_acceptable(sp.__version__, SCIPY_VERSION)


def is_sklearn_version_acceptable():
    return __is_version_acceptable(sa.__version__, SKLEARN_VERSION)


def get_recommended_library_versions():
    return {
        'pandas': PANDAS_VERSION,
        'numpy': NUMPY_VERSION,
        'matplotlib': MATPLOTLIB_VERSION,
        'seaborn': SEABORN_VERSION,
        'fitter': FITTER_VERSION,
        'scipy': SCIPY_VERSION,
        'sklearn': SKLEARN_VERSION
    }


def check_requirements():
    pass


def __raise_error_if_version_unacceptable(library_name: str):
    raise ValueError(f'{library_name}')


def __is_version_acceptable(version: str, minimum_version: str) -> bool:
    assertions.has_length(version, 'version')
    assertions.has_length(minimum_version, 'minimum version')
    return __compare(version, minimum_version) < 0


def __compare(version1: str, version2: str) -> int:
    version1_list = version1.split(DOT)
    version1_length = len(version1_list)
    version1_list = [int(value) for value in version1_list]

    version2_list = version2.split(DOT)
    version2_length = len(version2_list)
    version2_list = [int(value) for value in version2_list]

    if version1_length > version2_length:
        for _ in range(version2_length, version1_length):
            version2_list.append(0)

    elif version2_length > version1_length:
        for _ in range(version1_length, version2_length):
            version1_list.append(0)

    for i in range(version1_length):
        if version1_list[i] > version2_list[i]:
            return 1
        elif version2_list[i] > version1_list[i]:
            return -1
    return 0
