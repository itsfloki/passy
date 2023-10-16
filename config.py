from typing import List


class Config:
    """A class for managing command-line arguments."""

    def __init__(self, args: List[str]):
        self._option, self._value = self._parse_arguments(args)

    def option(self) -> str:
        return self._option

    def value(self) -> str:
        return self._value

    def _parse_arguments(self, args: List[str]):
        args_iter = iter(args)

        option = next(args_iter, None)
        value = next(args_iter, None)

        if not option:
            raise ValueError("Please provide an option")
        if (not value) and (option != "configure"):
            raise ValueError("Please provide a value")
        return option, value
