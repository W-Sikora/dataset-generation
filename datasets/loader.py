from os import path
from pandas import DataFrame, read_csv, to_datetime
from typing import Callable

DIRECTORY = 'data'


def load_covid(number_of_rows: int = None, preprocessing: bool = True) -> DataFrame:
    return load('covid.csv', number_of_rows, preprocess_covid if preprocessing else None)


def load_apartments(number_of_rows: int = None, preprocessing: bool = True) -> DataFrame:
    return load('apartments.csv', number_of_rows, preprocess_apartments if preprocessing else None)


def preprocess_covid(covid: DataFrame):
    covid = covid.dropna()
    date_key = 'Date'
    covid[date_key] = to_datetime(covid[date_key])
    columns = covid.columns.values.tolist()
    columns.remove(date_key)
    for column in columns:
        covid[column] = covid[column].astype(int)


def preprocess_apartments(apartments: DataFrame):
    apartments = apartments.dropna()
    apartments['Date'] = to_datetime(apartments['Date'])
    apartments['Precinct'] = apartments['Precinct'].astype(int).astype('category')
    apartments['Rooms'] = apartments['Rooms'].astype(int)
    apartments['Storey'] = apartments['Storey'].astype(int)


def load(dataset: str, number_of_rows: int = None, preprocess: Callable = None) -> DataFrame:
    dataset_path = path.join(DIRECTORY, dataset)
    dataset = read_csv(dataset_path, nrows=number_of_rows)
    if preprocess is not None:
        preprocess(dataset)
    return dataset
