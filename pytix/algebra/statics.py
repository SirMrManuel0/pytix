import numpy as np

from pytix.errors import TypesTuple, assertion, ArgumentError, ArgumentCodes
from pytix.types import Number

def rnd(x: Number) -> float:
    assertion.assert_types(x, TypesTuple.NUMBER.value, ArgumentError, code=ArgumentCodes.NOT_NUMBER)
    return float(np.round(x, 8))
