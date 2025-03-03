"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""
EXPECTED_BAKE_TIME = 40
PREPARATIO_TIME= 2
def bake_time_remaining(elapsed_baking_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_baking_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the Prep time in minutes.

    :param number_of_layers: int - number of layers in the lasagna being preped.
    :return: int - Time it will take to prep the lasagna derived from the constant 'PREPARATIO_TIME'.

    Function that takes how many layers the lasagna has as an argument and returns how much time it
    will take based on the constant 'PREPARATIO_TIME'.
    """
    return number_of_layers*PREPARATIO_TIME 

def elapsed_time_in_minutes(number_of_layers, elapsed_baking_time):
    """Calculate the elapsed time in minutes of the total preparation of the lasagna.

    :param number_of_layers: int - number of layers in the lasagna being preped.
    :param elapsed_time_in_minutes: int - baking time already elapsed.
    :return: int - total time (in minutes) it will take to preped and cook and the lasagna.

    Function that takes the numbers of layers and their correspondent prepep time combined with the
    elapsed time of baking as an argument and returns the total elapsed time the lasagna has been
    worked on.
    """
    return preparation_time_in_minutes(number_of_layers)+elapsed_baking_time
    
