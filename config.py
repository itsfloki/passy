class Config:
    """Keep track of cli argumetns"""

    def __init__(self, args: [str]):
        args_iter = iter(args)

        option = next(args_iter, None)
        label = next(args_iter, None)

        if not option:
            raise Exception("Please provide an option")
        if (not label) and (option != "configure"):
            raise Exception("Please provide a lable")

        self._option = option
        self._label = label

    def option(self):
        return self._option

    def label(self):
        return self._label
