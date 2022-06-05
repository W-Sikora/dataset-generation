from os.path import join, dirname
from typing import Callable

from pandas import DataFrame, read_csv, to_datetime


def load_covid(number_of_rows: int = None, preprocessing: bool = True) -> DataFrame:
    return __load('covid.csv', number_of_rows, __preprocess_covid if preprocessing else None)


def load_apartments(number_of_rows: int = None, preprocessing: bool = True) -> DataFrame:
    return __load('apartments.csv', number_of_rows, __preprocess_apartments if preprocessing else None)


def __preprocess_covid(dataset: DataFrame):
    covid = dataset.dropna().copy()
    date_key = 'Date'
    covid[date_key] = to_datetime(covid[date_key])
    columns = covid.columns.values.tolist()
    columns.remove(date_key)
    for column in columns:
        covid[column] = covid[column].astype(int)
    return covid


def __preprocess_apartments(dataset: DataFrame):
    apartments = dataset.dropna().copy()
    apartments['Date'] = to_datetime(apartments['Date'])
    apartments.update(apartments['Precinct'].astype(int).astype('category'))
    apartments.update(apartments['Rooms'].astype(int))
    apartments.update(apartments['Storey'].astype(int))
    return apartments


def __load(dataset: str, number_of_rows: int = None, preprocess: Callable = None) -> DataFrame:
    dataset_path = join(dirname(__file__), join('data', dataset))
    dataset = read_csv(dataset_path, nrows=number_of_rows)
    return preprocess(dataset) if preprocess is not None else dataset
