
import evaluation_prep as fortnite


def test_functions():
    assert fortnite.makesum(6, 4) == 10

def test_other():
    assert fortnite.listsum([2, 7, 78, -80]) == 7


def test_again():
    assert fortnite.make_dict(["hello", "hi", "joe", "hello"]) == {"hello": 2, "hi": 1, "joe": 1}






