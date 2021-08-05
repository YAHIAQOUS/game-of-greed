import pytest
from game_of_greed.game_logic import GameLogic

pytestmark = [pytest.mark.version_3]


@pytest.mark.parametrize(
    "test_input,expected",
    [
       (tuple(), tuple()),
        ((1,), (1,)),
        ((5,), (5,)),
        ((1, 2), (1,)),
        ((1, 1), (1,1)),
        ((1, 2, 3), (1,)),
        ((3, 3, 3, 5), (3, 3, 3, 5)),
        ((3, 3, 3, 3), (3, 3, 3, 3)),
        ((4, 4, 4, 4, 4), (4, 4, 4, 4, 4)),
        ((1, 6, 1, 6, 1, 6), (1, 1, 1, 6, 6, 6)),
        ((1, 2, 4, 3, 5, 6), (1, 2, 3, 4, 5, 6)),
        ((1, 1, 4, 4, 6, 6), (1, 1, 4, 4, 6, 6)),
        ((1, 2, 3, 5), (1, 5)),
        ((5, 1, 2, 3), (1, 5)),
        ((2, 3, 4), tuple()),
    ],
)
def test_get_scorers(test_input, expected):
    actual = GameLogic.get_scorers(test_input)
    assert sorted(actual) == sorted(expected)
