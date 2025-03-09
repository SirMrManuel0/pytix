import numpy as np

from useful_utility.errors import Types, TypesTuple, assertion, ArgumentError, ArgumentCodes

def rnd(x: Types.NUMBER.value) -> float:
    assertion.assert_types(x, TypesTuple.NUMBER.value, ArgumentError, code=ArgumentCodes.NOT_NUMBER)
    return float(np.round(x, 8))
