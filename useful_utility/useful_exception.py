class ArgumentError(Exception):
    def __init__(self, message: str = None, wrong_argument=None, correct_argument=None):
        if message is None:
            super().__init__(f"Invalid argument: {wrong_argument}. Expected an Argument such as: {correct_argument}.")
        else:
            super().__init__(message)
        self.wrong_argument = wrong_argument
        self.correct_argument = correct_argument

