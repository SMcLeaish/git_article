# %%
import pandas as pd
from pandas._libs.interval import VALID_CLOSED

print('Hello')
# %%
from statistics import median

print(median([5, 2, 3, 7]))
# %%


def validate_user_input(text: str, num: int) -> bool:
    """Validate two input arguments, a str and an int.

    Return True if both arguments are valid, False otherwise.

    Returns (bool)

    """
    return isinstance(text, str) and isinstance(num, int)


print(validate_user_input('bob', 'Jeff'))


def evenly_divisible():
    """Validate if positional argument is evenly divisible by divisor

    Inputs:

        divisor (int, default 2)
    Returns (bool)
    """
    pass
