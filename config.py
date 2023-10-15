from typing import List


class Config:
    """A class for managing command-line arguments."""

    def __init__(self, args: List[str]):
        self._option, self._label = self._parse_arguments(args)

    def option(self):
        return self._option

    def label(self):
        return self._label

    def _parse_arguments(self, args: List[str]):
        args_iter = iter(args)

        option = next(args_iter, None)
        label = next(args_iter, None)

        if not option:
            raise ValueError("Please provide an option")
        if (not label) and (option != "configure"):
            raise ValueError("Please provide a lable")
        return option, label
