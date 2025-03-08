from enum import Enum

import numpy as np


class Types(Enum):
    INT: tuple = (int, np.integer)
    FLOAT: tuple = (float, np.floating)
    NUMBER: tuple = (*INT, *FLOAT)
    LIST: tuple = (list,)
    TUPLE: tuple = (tuple,)
    ND_ARRAY: tuple = (np.ndarray,)
    LISTS: tuple = (*LIST, *ND_ARRAY)

class BaseCodes(Enum):
    NONE: int = 0
    TODO: int = 1

class BaseError(Exception):
    def __init__(self, code, msg="", wrong=None, right=None, err: str = "Error"):
        if wrong is not None:
            msg += f"\nWrong: {wrong}"
        if right is not None:
            msg += f"\nRight (Pattern): {right}"
        self.wrong = wrong
        self.right = right
        self.msg = msg
        super().__init__(f"{err} {code}: {msg}")

class ArgumentCodes(Enum):
    NONE: int = 0
    ZERO: int = 1
    LIST_LAYER_NOT_NUMBER: int = 2
    OUT_OF_RANGE: int = 3
    NOT_NUMBER: int = 4
    NOT_INT: int = 5
    NOT_LISTS: int = 6
    NOT_POSITIV: int = 7
    LIST_LAYER_NOT_NUMBER_LISTS: int = 8
    NOT_MATRIX_NP_ARRAY: int = 9
    NOT_EQUAL: int = 10
    MISMATCH_DIMENSION: int = 11
    NOT_TUPLE_LIST_ND_ARRAY: int = 12
    NOT_FLOAT: int = 13
    UNEXPECTED_TYPE: int = 14
    NOT_AXIS: int = 15
    NOT_VECTOR3D: int = 16

# current max: 21
class ArgumentError(BaseError):
    def __init__(self, code: ArgumentCodes, msg="", wrong_argument=None, right_argument=None):
        super().__init__(code, msg, wrong_argument, right_argument, "Argument Error")

class MathCodes(Enum):
    NONE: int = 0
    UNFIT_DIMENSIONS: int = 1
    NOT_MATRIX: int = 2
    NOT_MATRIX_NUMBER: int = 3
    NOT_NUMBER: int = 4
    NOT_FALSE: int = 5
    NOT_POSITIV: int = 6
    NOT_INT: int = 7
    NOT_VECTOR: int = 8
    NOT_DEFINED: int = 9
    ZERO: int = 10
    NOT_VECTOR_NUMBER: int = 11
    VECTOR: int = 12

# current max: 1
class MathError(BaseError):
    def __init__(self, code: MathCodes, msg="", wrong_argument=None, right_argument=None):
        super().__init__(code, msg, wrong_argument, right_argument, "Math Error")

def TODO(func):
    def wrapper(*args, **kwargs):
        raise BaseError(BaseCodes.TODO, "This function has yet to be fully or partially implemented!")
    return wrapper
