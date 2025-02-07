from unittest.mock import patch

import pytest

from pterminal.cursor import Cursor


@pytest.fixture
def mock_print():
    # Mock the built-in print function
    with patch("builtins.print") as mock_print:
        yield mock_print


def test_show_hide_cursor(mock_print):
    assert Cursor._state == "SHOW"
    Cursor.hide()
    mock_print.assert_called_once_with("\033[?25l", end="")
    mock_print.reset_mock()
    assert Cursor._state == "HIDE"
    Cursor.show()
    mock_print.assert_called_once_with("\033[?25h", end="")
    assert Cursor._state == "SHOW"
