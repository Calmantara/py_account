from app.main.util.helper.num import sum_int

import pytest


@pytest.mark.parametrize(
    "a,b,expected",
    [
        # test cases
        pytest.param(1, 2, 3, id="positif_integer"),
        pytest.param(-1, 2, 1, id="negative_positif_integer"),
        pytest.param(1, -2, -1, id="positif_negative_integer"),
        pytest.param(-1, -2, -3, id="negative_negative_integer"),
    ],
)
def test_sum_int(a, b, expected):
    res = sum_int(a, b)
    assert res == expected


# formatting
# python -> linter:
#  - pep8
#  - black
#  - flake8
