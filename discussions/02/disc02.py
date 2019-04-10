
import numpy as np
import pandas as pd
import os


def question01(data, labels):
    """
    Returns a dataframe from the
    given data (a dictionary of lists),
    and list of labels.

    >>> data = {'column1': [0,3,5,6], 'column2': [1,3,2,4]}
    >>> labels = 'a b c d'.split()
    >>> out = question01(data, labels)
    >>> isinstance(out, pd.DataFrame)
    True
    >>> out.index.tolist() == labels
    True
    """

    return ...


def question02(ser):
    """
    Given a Pandas Series, outputs the
    positions (an index or array) of 
    entries of ser that are multiples of 3.

    >>> ser = pd.Series([1, 3, 6, 9])
    >>> out = question02(ser)
    >>> out.tolist() == [1, 2, 3]
    True
    """

    return ...


def question03(df):
    """
    Returns the column name of the column column of df
    with the largets number of missing values.

    :param: df is a dataframe

    >>> df = pd.DataFrame({'col1': [np.NaN, np.NaN, 0], 'col2': [1, 2, 3]})
    >>> question03(df)
    'col1'
    """

    return ...


def question04(cars):
    """
    For the dataframe cars in the notebook,
    return a Series with three entries:
    1. The manufacturer with the highest price
    2. The model with the highest price
    3. The car type with the highest price,
    
    >>> url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
    >>> cars = pd.read_csv(url)
    >>> out = question04(cars)
    >>> isinstance(out, pd.Series)
    True
    >>> 'Manufacturer' in out.index
    True
    """

    return ...
