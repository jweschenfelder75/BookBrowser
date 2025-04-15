import re

class InputValidator():
    def validate_pattern_input(self, text: str, /) -> str | None:
        """
        Asks the user for input using the given prompt text.
        Validates whether the input is a valid regular expression pattern.

        Args:
            text (str): prompt text displayed to the user

        Returns:
            str | None: validated pattern string if valid, otherwise None
        """
        result = None
        while True:
            inp = input(text)
            if inp.isprintable() and self.is_valid_regex(inp):
                result = inp
            return result


    def is_valid_regex(self, pattern: str) -> bool:
        """
        Checks if a given RegEx pattern is valid.

        Args:
            pattern (str): pattern

        Returns:
            True if RegEx pattern is valid, otherwise False
        """
        try:
            re.compile(pattern)
            return True
        except re.error:
            return False


    def validate_int_with_exit_input(self, text: str, min_value: int, max_value: int, /) -> str:
        """
        Asks the user for input using the given prompt text.
        Validates whether the input is a valid number between min_value and max_value.

        Args:
            text (str): prompt text displayed to the user
            min_value (int): minimum value for a valid number
            max_value (int): maximum value for a valid number

        Returns:
            str: validated number as string, or exit command
        """
        result = None
        while True:
            inp = input(text)
            inp_chk = inp.strip().lower()
            if inp_chk in ("e", "exit"):
                result = inp_chk
            elif inp_chk.isnumeric() and min_value <= int(inp_chk) <= max_value:
                result = inp.strip()
            return result


    def validate_yesno_with_exit_input(self, text: str, /) -> str:
        """
        Asks the user for input using the given prompt text.
        Validates whether the input is a j/ja/n/nein (case-insensitive), or it is the exit command.

        Args:
            text (str): prompt text displayed to the user

        Returns:
            str: validated input string
        """
        while True:
            inp = input(text)
            inp_chk = inp.strip().lower()
            if inp_chk in ("j", "ja", "n", "nein", "e", "exit"):
                result = inp_chk
                return result


    def validate_yesno_input(self, text: str, /) -> str:
        """
        Asks the user for input using the given prompt text.
        Validates whether the input is a j/ja/n/nein (case-insensitive).

        Args:
            text (str): prompt text displayed to the user

        Returns:
            str: validated input string
        """
        while True:
            inp = input(text)
            inp_chk = inp.strip().lower()
            if inp_chk in ("j", "ja", "n", "nein"):
                result = inp_chk
                return result
