import pytest
from datetime import datetime

@pytest.fixture
def current_time():
    return datetime.now()


def test_foo(current_time):
    print(current_time)


def test_bar(current_time):
    print(current_time)


test_foo(current_time)
test_bar(current_time)
