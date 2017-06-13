import pandas as pd


def equal_operator(ds1, ds2):
    """
    Enter your code here
    """
    return (pd.Series(ds1) == pd.Series(ds2))


def greater_than_operator(ds1, ds2):
    """
    Enter your code here
    """
    return (pd.Series(ds1) > pd.Series(ds2))

def less_than_operator(ds1, ds2):
    """
    Enter your code here
    """
    return (pd.Series(ds1) < pd.Series(ds2))
