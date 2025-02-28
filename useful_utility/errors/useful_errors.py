from enum import Enum

class BaseCodes(Enum):
    NONE: int = 0
    TODO: int = 1

class BaseError(Exception):
    def __init__(self, code, msg=""):
        super().__init__(f"Error {code}: {msg}")

class ArgumentCodes(Enum):
    NONE: int = 0
    ZERO: int = 1
    LIST_LAYER_NOT_INT_FLOAT: int = 2
    OUT_OF_RANGE: int = 3
    NOT_INT_FLOAT: int = 4
    NOT_INT: int = 5
    NOT_LIST_NP_ARRAY: int = 6
    NOT_POSITIV: int = 7
    LIST_LAYER_NOT_INT_FLOAT_LIST_ND_ARRAY: int = 8
    NOT_MATRIX_NP_ARRAY: int = 9
    NOT_EQUAL: int = 10
    MISMATCH_DIMENSION: int = 11
    NOT_TUPLE_LIST_ND_ARRAY: int = 12
    NOT_FLOAT: int = 13

# current max: 21
class ArgumentError(BaseError):
    def __init__(self, code: ArgumentCodes, msg=None, wrong_argument=None, right_argument=None):
        if msg is None:
            msg: str = f"Argument Error!"
        if wrong_argument is not None:
            msg += f"\nWrong Argument: {wrong_argument}"
        if right_argument is not None:
            msg += f"\nRight Argument (Pattern): {right_argument}"
        self.wrong_argument = wrong_argument
        self.right_argument = right_argument
        self.msg = msg
        super().__init__(code, msg)

class MathCodes(Enum):
    NONE: int = 0
    UNFIT_DIMENSIONS: int = 1
    NOT_MATRIX: int = 2
    NOT_MATRIX_INT_FLOAT: int = 3
    NOT_INT_FLOAT: int = 4
    NOT_FALSE: int = 5
    NOT_POSITIV: int = 6
    NOT_INT: int = 7
    NOT_VECTOR: int = 8
    NOT_DEFINED: int = 9
    ZERO: int = 10

# current max: 1
class MathError(BaseError):
    def __init__(self, code: MathCodes, msg=None, wrong_argument=None, right_argument=None):
        if msg is None:
            msg: str = f"Math Error!"
        if wrong_argument is not None:
            msg += f"\nWrong Argument: {wrong_argument}"
        if right_argument is not None:
            msg += f"\nRight Argument (Pattern): {right_argument}"
        self.wrong_argument = wrong_argument
        self.right_argument = right_argument
        self.msg = msg
        super().__init__(code, msg)

def TODO(func):
    def wrapper(*args, **kwargs):
        raise BaseError(BaseCodes.TODO, "This function has yet to be fully or partially implemted!")
    return wrapper