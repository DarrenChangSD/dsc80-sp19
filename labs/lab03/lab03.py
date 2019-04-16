
import os

import pandas as pd
import numpy as np


# ---------------------------------------------------------------------
# Question # 1
# ---------------------------------------------------------------------

def blackjack_null_hypoth():
    """
    Returns a list of valid null hypotheses.
    
    :Example:
    >>> set(blackjack_null_hypoth()) <= set(range(1,11))
    True
    """
    return ...


def blackjack_alt_hypoth():
    """
    Returns a list of valid alternative hypotheses.
    
    :Example:
    >>> set(blackjack_alt_hypoth()) <= set(range(1,11))
    True
    """
    return ...


def blackjack_test_stat():
    """
    Returns a list of valid test statistics.
    
    :Example:
    >>> set(blackjack_test_stat()) <= set(range(1,5))
    True
    """
    return ...


def blackjack_p_value():
    """
    Returns an integer corresponding to the correct explanation.
    
    :Example:
    >>> blackjack_p_value() in [1,2,3,4,5]
    True
    """
    return ...


# ---------------------------------------------------------------------
# Question #2
# ---------------------------------------------------------------------

def clean_apps(df):
    '''
    >>> fp = os.path.join('data', 'googleplaystore.csv')
    >>> df = pd.read_csv(fp)
    >>> cleaned = clean_apps(df)
    >>> len(cleaned) == len(df)
    True
    >>> cleaned.Reviews.dtype == int
    True
    '''
    
    return ...


def store_info(df):
    '''
    >>> fp = os.path.join('data', 'googleplaystore.csv')
    >>> df = pd.read_csv(fp)
    >>> cleaned = clean_apps(df)
    >>> info = store_info(cleaned)
    >>> len(info)
    3
    >>> info[2] in cleaned.Category.unique()
    True
    '''

    return ...

# ---------------------------------------------------------------------
# Question 3
# ---------------------------------------------------------------------


def describe_salaries_by_job_type(salaries):
    """
    >>> fp = os.path.join('data', 'san-diego-2017.csv')
    >>> salaries = pd.read_csv(fp)
    >>> out = describe_salaries_by_job_type(salaries)
    >>> cols = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']
    >>> (out.columns == cols).all()
    True
    """

    return ...


def std_salaries_by_job_type(salaries):
    """
    >>> fp = os.path.join('data', 'san-diego-2017.csv')
    >>> salaries = pd.read_csv(fp)
    >>> out = std_salaries_by_job_type(salaries)
    >>> set(out.columns) == set(['Base Pay', 'Overtime Pay', 'Total Pay', 'Job Type'])
    True
    >>> np.all(abs(out.select_dtypes(include='number').mean()) < 10**-7)  # standard units should average to 0!
    True
    """

    return ...


def salaries_spread():
    """
    >>> out = salaries_spread()
    >>> len(out) == 2
    True
    >>> out[1] in ['Police', 'Fire', 'Libr', 'Rec', 'Grounds', 'Lifeguard', 'Water', 'Equip', 'Utility', 'Clerical', 'Administrative', 'Sanitation', 'Principal', 'Public', 'Dispatcher', 'Other']
    True
    """
    return ...


# ---------------------------------------------------------------------
# Question #4
# ---------------------------------------------------------------------


def read_survey(dirname):
    """
    read_survey combines all the survey*.csv files into a singular DataFrame
    :param dirname: directory name where the survey*.csv files are
    :returns: a DataFrame containing the combined survey data
    :Example:
    >>> dirname = os.path.join('data', 'responses')
    >>> out = read_survey(dirname)
    >>> isinstance(out, pd.DataFrame)
    True
    >>> len(out)
    5000
    >>> read_survey('nonexistentfile') # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    FileNotFoundError: ... 'nonexistentfile'
    """

    return ...


def com_stats(df):
    """
    com_stats 
    :param df: a DataFrame containing the combined survey data
    :returns: a list containing the most common first name, job held, 
    university attended, and current company
    :Example:
    >>> dirname = os.path.join('data', 'responses')
    >>> df = read_survey(dirname)
    >>> out = com_stats(df)
    >>> len(out)
    4
    >>> all([isinstance(x, str) for x in out])
    True
    """

    return ...


# ---------------------------------------------------------------------
# Question #5
# ---------------------------------------------------------------------

def combine_surveys(dirname):
    """
    combine_surveys takes in a directory path 
    (containing files favorite*.csv) and combines 
    all of the survey data into one DataFrame, 
    indexed by student ID (a value 0 - 1000).

    :Example:
    >>> dirname = os.path.join('data', 'extra-credit-surveys')
    >>> out = combine_surveys(dirname)
    >>> isinstance(out, pd.DataFrame)
    True
    >>> out.shape
    (1000, 6)
    >>> combine_surveys('nonexistentfile') # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    FileNotFoundError: ... 'nonexistentfile'
    """

    return ...


def check_credit(df):
    """
    check_credit takes in a DataFrame with the 
    combined survey data and outputs a DataFrame 
    of the names of students and how many extra credit 
    points they would receive, indexed by their ID (a value 0-1000)

    :Example:
    >>> dirname = os.path.join('data', 'extra-credit-surveys')
    >>> df = combine_surveys(dirname)
    >>> out = check_credit(df)
    >>> out.shape
    (1000, 2)
    """

    return ...

# ---------------------------------------------------------------------
# Question # 6
# ---------------------------------------------------------------------


def at_least_once(pets, procedure_history):
    """
    How many pets have procedure performed at this clinic at least once.

    :Example:
    >>> pets_fp = os.path.join('data', 'pets', 'Pets.csv')
    >>> procedure_history_fp = os.path.join('data', 'pets', 'ProceduresHistory.csv')
    >>> pets = pd.read_csv(pets_fp)
    >>> procedure_history = pd.read_csv(procedure_history_fp)
    >>> out = at_least_once(pets, procedure_history)
    >>> out < len(pets)
    True
    """
    return ...


def pet_name_by_owner(owners, pets):
    """
    pet names by owner

    :Example:
    >>> owners_fp = os.path.join('data', 'pets', 'Owners.csv')
    >>> pets_fp = os.path.join('data', 'pets', 'Pets.csv')
    >>> owners = pd.read_csv(owners_fp)
    >>> pets = pd.read_csv(pets_fp)
    >>> out = pet_name_by_owner(owners, pets)
    >>> len(out) == len(owners)
    True
    >>> 'Sarah' in out.index
    True
    >>> 'Cookie' in out.values
    True
    """
    return ...


def total_cost_per_owner(owners, pets, procedure_history, procedure_detail):
    """
    total cost per owner

    :Example:
    >>> owners_fp = os.path.join('data', 'pets', 'Owners.csv')
    >>> pets_fp = os.path.join('data', 'pets', 'Pets.csv')
    >>> procedure_detail_fp = os.path.join('data', 'pets', 'ProceduresDetails.csv')
    >>> procedure_history_fp = os.path.join('data', 'pets', 'ProceduresHistory.csv')

    >>> owners = pd.read_csv(owners_fp)
    >>> pets = pd.read_csv(pets_fp)
    >>> procedure_detail = pd.read_csv(procedure_detail_fp)
    >>> procedure_history = pd.read_csv(procedure_history_fp)
    >>> out = total_cost_per_owner(owners, pets, procedure_history, procedure_detail)
    >>> set(out.index) <= set(owners['OwnerID'])
    True
    """

    return ...



# ---------------------------------------------------------------------
# DO NOT TOUCH BELOW THIS LINE
# IT'S FOR YOUR OWN BENEFIT!
# ---------------------------------------------------------------------


# Graded functions names! DO NOT CHANGE!
# This dictionary provides your doctests with
# a check that all of the questions being graded
# exist in your code!

GRADED_FUNCTIONS = {
    'q01': [
        'blackjack_null_hypoth', 'blackjack_alt_hypoth',
        'blackjack_test_stat', 'blackjack_p_value'
    ],
    'q02': ['clean_apps', 'store_info'],
    'q03': [
        'describe_salaries_by_job_type', 'std_salaries_by_job_type',
        'salaries_spread'],
    'q04': ['read_survey', 'com_stats'],
    'q05': ['combine_surveys', 'check_credit'],
    'q06': ['at_least_once', 'pet_name_by_owner', 'total_cost_per_owner']
}


def check_for_graded_elements():
    """
    >>> check_for_graded_elements()
    True
    """
    
    for q, elts in GRADED_FUNCTIONS.items():
        for elt in elts:
            if elt not in globals():
                stmt = "YOU CHANGED A QUESTION THAT SHOULDN'T CHANGE! \
                In %s, part %s is missing" % (q, elt)
                raise Exception(stmt)

    return True
