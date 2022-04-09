from os import path
from pandas import DataFrame, Categorical, read_csv, to_datetime

from datasets.language_option import LanguageOption


class Loader:

    def __init__(self,

                 language_option: LanguageOption = LanguageOption.ENGLISH):
        self.language_option = language_option


ENGLISH = 'en'
POLISH = 'pl'
MIN_ROWS = 1


def __load(dataset_name: str, number_of_rows: int = None) -> DataFrame:
    dataset_path = path.join('datasets', 'data', dataset_name)

    return read_csv(
        dataset_path,
        nrows=number_of_rows,
        header=None
    )


def __validate_headers_language(headers_language: str):
    if headers_language != ENGLISH and headers_language != POLISH:
        raise Exception(f'The allowed values are \'{ENGLISH}\' or \'{POLISH}\'')


def __validate_number_of_rows(number_of_rows: int, max_rows: int):
    if number_of_rows is not None and MIN_ROWS > number_of_rows > max_rows:
        raise Exception(f'The number of rows must be between {MIN_ROWS} and {max_rows}')


def __form_dataset(dataset_name: str, headers: dict, max_number_of_rows: int,
                   headers_language: str = 'en', number_of_rows: int = None) -> DataFrame:
    __validate_headers_language(headers_language)
    __validate_number_of_rows(number_of_rows, max_number_of_rows)

    date_column_name = 0
    dataset = __load(dataset_name, number_of_rows)
    dataset[date_column_name] = to_datetime(dataset[date_column_name])
    dataset.columns = headers[headers_language]

    return dataset


def __load_stock_market(dataset_name: str, headers_language: str = 'en', number_of_rows: int = None) -> DataFrame:
    stock_market_max_number_of_rows = 429
    stock_market_headers = {
        ENGLISH: [
            'Date',
            'Open',
            'High',
            'Low',
            'Close',
            'Adj Close',
            'Volume',
        ],
        POLISH: [
            'Data',
            'Otwarcie',
            'Najwyższa',
            'Najniższa',
            'Zamknięcie',
            'Skorygowana cena zamknięcia',
            'Wolumen'
        ]
    }

    return __form_dataset(dataset_name, stock_market_headers, stock_market_max_number_of_rows,
                          headers_language, number_of_rows)


def load_mcr(headers_language: str = 'en', number_of_rows: int = None) -> DataFrame:
    """
    :return: DataFrame
        Date         datetime64[ns]
        Open                float64
        High                float64
        Low                 float64
        Close               float64
        Adj Close           float64
        Volume              float64
    """
    dataset_name = 'mcr.csv'

    return __load_stock_market(dataset_name, headers_language, number_of_rows)


def load_bml(headers_language: str = 'en', number_of_rows: int = None) -> DataFrame:
    """
    :return: DataFrame
        Date         datetime64[ns]
        Open                float64
        High                float64
        Low                 float64
        Close               float64
        Adj Close           float64
        Volume              float64
    """
    dataset_name = 'bml.csv'

    return __load_stock_market(dataset_name, headers_language, number_of_rows)


def load_covid(headers_language: str = 'en', number_of_rows: int = None) -> DataFrame:
    """
    :return: DataFrame
        Date                       datetime64[ns]
        New cases                           int64
        All cases                           int64
        Deaths                              int64
        All deaths                          int64
        Convalescent                        int64
        All convalescent                    int64
        All quarantined persons             int64
    """
    dataset_name = 'covid.csv'
    max_number_of_rows = 599
    headers = {
        ENGLISH: [
            'Date',
            'New cases',
            'All cases',
            'Deaths',
            'All deaths',
            'Convalescent',
            'All convalescent',
            'All quarantined persons'
        ],
        POLISH: [
            'Data',
            'Nowe przypadki',
            'Wszystkie przypadki',
            'Zgony',
            'Wszystkie zgony',
            'Ozdrowieńcy',
            'Wszyscy ozdrowieńcy',
            'Wszystkie osoby poddane kwarantannie'
        ]
    }

    return __form_dataset(dataset_name, headers, max_number_of_rows,
                          headers_language, number_of_rows)


def load_apartments(headers_language: str = 'en', number_of_rows: int = None) -> DataFrame:
    """
    :return: DataFrame
        Transaction date    datetime64[ns]
        Precinct                  category
        Apartment area             float64
        Number of rooms            float64
        Storey                     float64
        Selling price              float64
    """
    dataset_name = 'apartments.csv'
    max_number_of_rows = 5_666
    precinct = {
        ENGLISH: 'Precinct',
        POLISH: 'Obwód'
    }
    headers = {
        ENGLISH: [
            'Transaction date',
            precinct[ENGLISH],
            'Apartment area',
            'Number of rooms',
            'Storey',
            'Selling price'
        ],
        POLISH: [
            'Data transakcji',
            precinct[POLISH],
            'Powierzchnia mieszkania',
            'Liczba pokoi',
            'Piętro',
            'Cena sprzedaży'
        ]
    }

    categorical_column_name = precinct[headers_language]
    dataset = __form_dataset(dataset_name, headers, max_number_of_rows, headers_language, number_of_rows)
    dataset[categorical_column_name] = Categorical(dataset[categorical_column_name])

    return dataset
