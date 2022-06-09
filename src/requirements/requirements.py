from platform import python_version
from typing import Dict

import fitter as ft
import matplotlib as mp
import numpy as np
import pandas as pd
import scipy as sp
import seaborn as sn
import sklearn as sa

import src.utils.assertions as assertions
from src.utils.string_utils import DOT

PYTHON_VERSION = '3.7.7'
PANDAS_VERSION = '1.2.3'
NUMPY_VERSION = '1.19.5'
MATPLOTLIB_VERSION = '3.3.3'
SEABORN_VERSION = '0.11.2'
FITTER_VERSION = '1.4.0'
SCIPY_VERSION = '1.7.3'
SKLEARN_VERSION = '1.0.2'

MESSAGE = 'you are using {} {} version, version {} or higher is required'


def get_recommended_versions() -> Dict[str, str]:
    return {
        'Python': PYTHON_VERSION,
        'Pandas': PANDAS_VERSION,
        'NumPy': NUMPY_VERSION,
        'Matplotlib': MATPLOTLIB_VERSION,
        'Seaborn': SEABORN_VERSION,
        'Fitter': FITTER_VERSION,
        'SciPy': SCIPY_VERSION,
        'Scikit-learn': SKLEARN_VERSION
    }


def check_requirements():
    __python_version_acceptable()
    __pandas_version_acceptable()
    __numpy_version_acceptable()
    __matplotlib_version_acceptable()
    __seaborn_version_acceptable()
    __fitter_version_acceptable()
    __scipy_version_acceptable()
    __sklearn_version_acceptable()


def __python_version_acceptable():
    version = python_version()
    if not __is_version_acceptable(version, PYTHON_VERSION):
        raise ValueError(MESSAGE.format('Python', version, PYTHON_VERSION))


def __pandas_version_acceptable():
    version = pd.__version__
    if not __is_version_acceptable(version, PANDAS_VERSION):
        raise ValueError(MESSAGE.format('Pandas', version, PANDAS_VERSION))


def __numpy_version_acceptable():
    version = np.__version__
    if not __is_version_acceptable(version, NUMPY_VERSION):
        raise ValueError(MESSAGE.format('NumPy', version, NUMPY_VERSION))


def __matplotlib_version_acceptable():
    version = mp.__version__
    if not __is_version_acceptable(version, MATPLOTLIB_VERSION):
        raise ValueError(MESSAGE.format('Matplotlib', version, MATPLOTLIB_VERSION))


def __seaborn_version_acceptable():
    version = sn.__version__
    if not __is_version_acceptable(version, SEABORN_VERSION):
        raise ValueError(MESSAGE.format('Seaborn', version, SEABORN_VERSION))


def __fitter_version_acceptable():
    version = ft.version
    if not __is_version_acceptable(version, FITTER_VERSION):
        raise ValueError(MESSAGE.format('Fitter', version, FITTER_VERSION))


def __scipy_version_acceptable():
    version = sp.__version__
    if not __is_version_acceptable(version, SCIPY_VERSION):
        raise ValueError(MESSAGE.format('SciPy ', version, SCIPY_VERSION))


def __sklearn_version_acceptable():
    version = sa.__version__
    if not __is_version_acceptable(version, SKLEARN_VERSION):
        raise ValueError(MESSAGE.format('Scikit-learn', version, SKLEARN_VERSION))


def __is_version_acceptable(version: str, minimum_version: str) -> bool:
    assertions.has_length(version, 'version')
    assertions.has_length(minimum_version, 'minimum version')
    return __compare(version, minimum_version) >= 0


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
