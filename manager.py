import random
import string


class Manager:
    """A class for managing passwords."""

    def __init__(self, label: str):
        self._label = label

    def _generate(self, length: int) -> str:
        population = string.ascii_letters + string.digits + "#$@"
        return ''.join(random.sample(population, length))

    def create(self, length: int) -> str:
        return self._generate(length)

    def view(self) -> str:
        # TODO: implement this
        pass

    def delete(self) -> str:
        # TODO: implement this
        pass
