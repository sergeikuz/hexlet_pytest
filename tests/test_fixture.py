import pytest
from hexlet_pytest.function_for_fxture import compact, select


@pytest.fixture
def coll():
    return ['One', True, 3, [1, 'hexlet', [0]], 'cat', {}, '', [], False]


def test_compact(coll):
    result = compact(coll)
    assert result == ['One', True, 3]


def test_select(coll):
    result = select(coll)
    assert result == [[1, 'hexlet', [0]], 'cat', {}, '', [], False]

