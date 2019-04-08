
import os
import pandas as pd
import numpy as np

# ---------------------------------------------------------------------
# Question #1
# ---------------------------------------------------------------------

def normalize_hw(grades):
    """
    normalize_hw takes in a dataframe like grades
    and outputs a dataframe of normalized HW grades.
    The output should not take the late penalty into account.

    :Example:
    >>> fp = os.path.join('data', 'grades.csv')
    >>> grades = pd.read_csv(fp)
    >>> hw = normalize_hw(grades)
    >>> np.all(hw.columns == ['hw0%d' % d for d in range(1,10)])
    True
    >>> len(grades) == len(hw)
    True
    >>> np.all(np.isclose(hw.mean(), 0.80, atol=10))
    True
    """

    return ...


# ---------------------------------------------------------------------
# Question #2
# ---------------------------------------------------------------------


def last_minute_submissions(grades):
    """
    last_minute_submissions takes in the dataframe 
    grades and a Series indexed by HW assignment that 
    contains the number of submissions that were turned 
    in on time by the student, yet marked 'late' by Gradescope.

    :Example:
    >>> fp = os.path.join('data', 'grades.csv')
    >>> grades = pd.read_csv(fp)
    >>> out = last_minute_submissions(grades)
    >>> isinstance(out, pd.Series)
    True
    >>> np.all(out.index == ['hw0%d' % d for d in range(1,10)])
    True
    >>> (out > 0).sum()
    8
    """

    return ...


# ---------------------------------------------------------------------
# Question #3
# ---------------------------------------------------------------------


def adjust_lateness(grades):
    """
    adjust_lateness takes in the dataframe like `grades` 
    and returns a dataframe of HW grades adjusted for 
    lateness according to the syllabus.

    :Example:
    >>> fp = os.path.join('data', 'grades.csv')
    >>> grades = pd.read_csv(fp)
    >>> out = adjust_lateness(grades)
    >>> isinstance(out, pd.DataFrame)
    True
    >>> out.loc[20, 'hw01'] != (grades.loc[20, 'hw01'] * 100)
    True
    """

    return ...


# ---------------------------------------------------------------------
# Question #4
# ---------------------------------------------------------------------


def hw_total(adjusted):
    """
    hw_total takes in a dataframe of lateness-adjusted 
    HW grades, and computes the total HW grade for 
    each student according to the syllabus.

    :Example:
    >>> fp = os.path.join('data', 'grades.csv')
    >>> grades = pd.read_csv(fp)
    >>> adj = adjust_lateness(grades)
    >>> out = hw_total(adj)
    >>> isinstance(out, pd.Series)
    True
    >>> np.all((0 <= out) & (1 >= out))
    True
    >>> out.notnull().all()
    True
    """

    return ...


# ---------------------------------------------------------------------
# Question #5
# ---------------------------------------------------------------------


def average_student(grades):
    """
    average_student takes in a dataframe 
    like `grades` and outputs the HW grade 
    of a student who received the average 
    grade on each HW assignment.

    :Example:
    >>> fp = os.path.join('data', 'grades.csv')
    >>> grades = pd.read_csv(fp)
    >>> out = average_student(grades)
    >>> import numbers
    >>> isinstance(out, numbers.Real)
    True
    >>> np.isclose(out, 80, atol=5)
    True
    """

    return ...


def higher_or_lower():
    """
    higher_or_lower returns either 'higher' or
    'lower' depending on whether a hypothetical
    average student does better on average than
    the average total HW score in the course.

    :Example:
    >>> higher_or_lower() in ['higher', 'lower']
    True
    """
    
    return ...


# ---------------------------------------------------------------------
# Question #6
# ---------------------------------------------------------------------


def extra_credit_total(grades):
    """
    extra_credit_total takes in a dataframe like `grades` 
    and returns the total extra-credit grade as a 
    proportion between 0 and 1.

    :Example:
    >>> fp = os.path.join('data', 'grades.csv')
    >>> grades = pd.read_csv(fp)
    >>> out = extra_credit_total(grades)
    >>> isinstance(out, pd.Series)
    True
    >>> np.all((0 <= out) & (1 >= out))
    True
    """

    return ...


# ---------------------------------------------------------------------
# Question #7
# ---------------------------------------------------------------------


def total_points(grades):
    """
    total_points takes in grades and returns 
    the final course grades according to the syllabus.

    :Example:
    >>> fp = os.path.join('data', 'grades.csv')
    >>> grades = pd.read_csv(fp)
    >>> out = total_points(grades)
    >>> isinstance(out, pd.Series)
    True
    >>> np.isclose(out.max(), 0.95, atol=0.05)
    True
    """

    return ...


def final_grades(total):
    """
    final_grades takes in the final course grades 
    as above and returns a Series of letter grades 
    given by the standard cutoffs.

    :Example:
    >>> out = final_grades(pd.Series([0.92, 0.81, 0.41]))
    >>> np.all(out == ['A', 'B', 'F'])
    True
    """
    
    return ...


def letter_proportions(grades):
    """
    letter_proportions takes in the dataframe grades 
    and outputs a Series that contains the proportion
    of the class that received each grade.

    :Example:
    >>> fp = os.path.join('data', 'grades.csv')
    >>> grades = pd.read_csv(fp)
    >>> out = letter_proportions(grades)
    >>> np.all(out.index == ['B', 'C', 'A', 'D', 'F'])
    True
    >>> out.sum() == 1.0
    True
    """

    return ...


# ---------------------------------------------------------------------
# Question # 8
# ---------------------------------------------------------------------


def simulate_pval(grades, N):
    """
    simulate_pval takes in the number of 
    simulations N and grades and returns 
    the likelihood that the grade of juniors 
    was no better on average than the class 
    as a whole (i.e. calculate the p-value).

    :Example:
    >>> fp = os.path.join('data', 'grades.csv')
    >>> grades = pd.read_csv(fp)
    >>> out = simulate_pval(grades, 100)
    >>> 0 <= out <= 0.1
    True
    """

    return ...


# ---------------------------------------------------------------------
# Question # 9
# ---------------------------------------------------------------------


def get_assignment_proportions(grades):
    """
    get_assignment_proportions takes in grades 
    and returns a dictionary keyed by assignment name
    with values given by the proportion of 
    the final grade that assignment makes up.

    :Example:
    >>> fp = os.path.join('data', 'grades.csv')
    >>> grades = pd.read_csv(fp)
    >>> out = get_assignment_proportions(grades)
    >>> 'project01_free_response' in out.keys()
    True
    >>> 'project03_checkpoint01' in out.keys()
    True
    >>> np.isclose(sum(out.values()), 1.0222, atol=0.01)
    True
    """
    
    return ...


# ---------------------------------------------------------------------
# Question #10
# ---------------------------------------------------------------------


def curved_total_points(grades):
    """
    curved_total_points takes in grades and outputs 
    the curved total scores for each student.

    :Example:
    >>> fp = os.path.join('data', 'grades.csv')
    >>> grades = pd.read_csv(fp)
    >>> out = curved_total_points(grades)
    >>> isinstance(out, pd.Series)
    True
    >>> out.max() < 2
    True
    >>> out.min() > -10
    True
    """
    
    return ...


def curved_letter_grades(curved_grades, prop):
    """
    curved_letter_grades which takes in:
        - a Series of curved course grades (as above),
        - a Series of letter grade distributions 
        (e.g. the output of letter_proportions)

    and returns a Series containing the letter grade of 
    each student according to the curve (as described in
    the notebook).

    :Example:
    >>> prop = pd.Series([0.2]*5, index='A B C D F'.split())
    >>> curved_grades = pd.Series([-0.2, 0, -0.5, 0.2, 2, -1, -3.1, 3, 0.4, 5])
    >>> out = curved_letter_grades(curved_grades, prop)
    >>> isinstance(out, pd.Series)
    True
    >>> distr = out.value_counts(normalize=True).sort_index()
    >>> np.all(distr == prop.sort_index())
    True
    >>> out.iloc[1] == 'C'
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
    'q01': ['normalize_hw'],
    'q02': ['last_minute_submissions'],
    'q03': ['adjust_lateness'],
    'q04': ['hw_total'],
    'q05': ['average_student', 'higher_or_lower'],
    'q06': ['extra_credit_total'],
    'q07': ['total_points', 'final_grades'],
    'q08': ['simulate_pval'],
    'q09': ['get_assignment_proportions'],
    'q10': ['curved_total_points', 'curved_letter_grades']
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
                In %s, part %s is missing" %(q, elt)
                raise Exception(stmt)

    return True
