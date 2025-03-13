import numpy as np

from useful_utility.errors import TypesTuple, assertion, ArgumentError, ArgumentCodes
from useful_utility.types import Number

def rnd(x: Number) -> float:
    assertion.assert_types(x, TypesTuple.NUMBER.value, ArgumentError, code=ArgumentCodes.NOT_NUMBER)
    return float(np.round(x, 8))
