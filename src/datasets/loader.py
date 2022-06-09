from os.path import join, dirname
from typing import Callable

from pandas import DataFrame, read_csv, to_datetime


def load_covid(number_of_rows: int = None,
               drop_missing_values: bool = True,
               preprocessing: bool = True) -> DataFrame:
    return __load(
        'covid.csv',
        number_of_rows,
        drop_missing_values,
        __preprocess_covid if drop_missing_values and preprocessing else None
    )


def load_apartments(number_of_rows: int = None,
                    drop_missing_values: bool = True,
                    preprocessing: bool = True) -> DataFrame:
    return __load(
        'apartments.csv',
        number_of_rows,
        drop_missing_values,
        __preprocess_apartments if drop_missing_values and preprocessing else None
    )


def __preprocess_covid(covid: DataFrame):
    date_key = 'Date'
    covid[date_key] = to_datetime(covid[date_key])
    columns = [covid.columns.values]
    columns.remove(date_key)
    for column in columns:
        covid[column] = covid[column].astype(int)
    return covid


def __preprocess_apartments(apartments: DataFrame):
    apartments['Date'] = to_datetime(apartments['Date'])
    apartments.update(apartments['Precinct'].astype(int).astype('category'))
    apartments.update(apartments['Rooms'].astype(int))
    apartments.update(apartments['Storey'].astype(int))
    return apartments


def __load(dataset: str,
           number_of_rows: int = None,
           drop_missing_values: bool = True,
           preprocess: Callable = None) -> DataFrame:
    dataset_path = join(dirname(__file__), join('data', dataset))
    dataset = read_csv(dataset_path, nrows=number_of_rows)

    if drop_missing_values:
        dataset = dataset.dropna().copy()

    if preprocess is None:
        return dataset

    return preprocess(dataset)
