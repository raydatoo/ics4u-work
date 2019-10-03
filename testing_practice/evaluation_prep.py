'''
Create two files: evaluation_prep.py and test_evaluation_prep.py. Your functions will go in evaluation_prep.py and your tests will go in test_evaluation_prep.py.

For each function below:

create the function
annotate the function
create a docstring
and create tests for the function.
Create a function that takes two integers a and b. The function will return the sum of the two integers.
Create a function that takes a list of integers and returns the sum of all the numbers.
Create a function that takes a list of words. Then create and return a dictionary where the key is the word and the value is how many times the word appears in the list.

'''

from typing import List


def makesum(num1: int, num2: int) -> int:

    '''
    Dis function add two numbers

    num1: an integer
    num2: another integer

    return: the sum of the two integers

    '''

    return num1+num2


def listsum(bleh: List[int]) -> int:

    '''
    dis function takes list and adds them

    bleh: list to addt

    return: int
    '''

    a = 0

    for i in bleh:
        a += i

    return a
