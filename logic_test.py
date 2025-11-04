import pytest

@pytest.fixture
def dataset():
    """Return some data to test functions"""
    return {'data1': 1, 'data2': 2}

def test_dataset(dataset):
    """test and confirm fixture value"""
    assert dataset == {'data1': 1, 'data2': 2}

def basic_math():
    assert 1+1 == 2
    assert 2*2 == 4
    assert 3**3 == 9


if __file__ == __main__:
    test_dataset(dataset())
    basic_math()
