from typing import List


class Config:
    """A class for managing command-line arguments."""

    def __init__(self, args: List[str]):
        self._option, self._value, self._length = self._parse_arguments(args)

    def option(self) -> str:
        return self._option

    def value(self) -> str:
        return self._value

    def length(self) -> str:
        return self._length

    def _parse_arguments(self, args: List[str]):
        args_iter = iter(args)

        option = next(args_iter, None)
        value = next(args_iter, None)
        length = next(args_iter, "15")

        if not option:
            raise ValueError("Please provide an option")
        if (not value) and (option != "configure"):
            raise ValueError("Please provide a value")
        if not length.isnumeric():
            raise ValueError("Please provide password length")
        return option, value, int(length)
