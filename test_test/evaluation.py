from typing import List


def float_avg(a: float, b: float, c: float) -> float:

    '''Takes three floats and returns their average

    Args:
        a: a float
        b: a float
        c: also a float (what a surprise)
    
    Returns:
        The average of the three given floats
    '''

    return (a+b+c)/3



def outcome_counter(game_list: List[str], result: str) -> int:

    '''Finds the number of times a chosen outcome is in a list of outcomes

    Args:
        game_list: a list of the outcomes of the games
        result: the desired outcome (W, L, or T)

    Returns:
        The number of times the desired outcome was in the list of outcomes

    '''

    counter = 0 
    for game in game_list:
        if game == result:
            counter += 1

    return counter



def sort_outcomes(game_list: List[str]) -> dict:

    '''Takes a list of game outcomes and sorts them into a dictionary

    Args:
        game_list: a list of game outcomes

    Returns:
        A sorted dictionary of the outcomes and the number of ocurrences

    '''

    game_dict = {"W": 0, "L": 0, "T": 0}

    wins = 0
    losses = 0
    ties = 0

    for game in game_list:
        if game == "W":
            wins += 1
        elif game == "L":
            losses += 1
        elif game == "T":
            ties += 1
    
    game_dict["W"] = wins
    game_dict["L"] = losses
    game_dict["T"] = ties

    return game_dict



def occurence_finder(game_dict: dict, result: str) -> int:

    '''Takes the key of a dictionary of outcomes and finds the value

    Args:
        game_dict: a list of the outcomes of the games
        result: the desired outcome (W, L, or T)

    Returns:
        The value of the key specified

    '''

    return game_dict[result]


