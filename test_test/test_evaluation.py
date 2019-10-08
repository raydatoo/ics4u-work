import evaluation as f


def test_float_avg():
    assert f.float_avg(2.0, 6.0, 7.0) == 5
    assert f.float_avg(3.5, 4.7, 0.8) == 3
    assert f.float_avg(5.9, 64.9, 37.5) == 36.1


def test_outcome_counter():
    assert f.outcome_counter(["W", "L", "T", "W", "W", "L", "T", "T", "T"], "T") == 4
    assert f.outcome_counter(["L", "L", "T", "L", "T", "L", "T", "T", "T"], "W") == 0
    assert f.outcome_counter(["L", "L", "L", "L", "L", "L", "L", "L", "L"], "L") == 9


def test_sort_outcomes():
    assert f.sort_outcomes(["W", "L", "T", "W", "W", "L", "T", "T", "T"]) == {'W': 3, 'L': 2, 'T': 4}
    assert f.sort_outcomes(["L", "L", "L", "L", "L", "L", "L", "L", "L"]) == {'W': 0, 'L': 9, 'T': 0}
    assert f.sort_outcomes(["W", "T", "L", "L", "T", "W", "L", "L", "T"]) == {'W': 2, 'L': 4, 'T': 3}


def test_occurance_finder():
    assert f.occurence_finder({'W': 3, 'L': 2, 'T': 4}, "W")
    assert f.occurence_finder({'W': 0, 'L': 9, 'T': 0}, "L")
    assert f.occurence_finder({'W': 2, 'L': 4, 'T': 3}, "T")