class Cursor(object):
    _state = "SHOW"

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
