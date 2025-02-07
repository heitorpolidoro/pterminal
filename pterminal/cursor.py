class Cursor(object):
    """
    Represents a Cursor object that allows manipulation of the terminal cursor.

    This class provides static methods to:
     - Show or hide the cursor in a terminal
    """

    _state: str = "SHOW"

    @staticmethod
    def hide() -> None:
        # Hide cursor
        print("\033[?25l", end="")
        Cursor._state = "HIDE"

    @staticmethod
    def show() -> None:
        # Show cursor
        print("\033[?25h", end="")
        Cursor._state = "SHOW"
