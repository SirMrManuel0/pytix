from typing import override, Self, Union

import numpy as np

from useful_utility.errors import ArgumentError, MathError, assertion
from useful_utility.errors import ArgumentCodes,  MathCodes, TODO, TypesTuple, Types
from useful_utility.algebra.matrix import Matrix
from useful_utility.algebra.statics import rnd


class Vector(Matrix):
    def __init__(self, coordinates=None, dimension: Types.INT.value = 2):
        assertion.assert_types(dimension, TypesTuple.INT.value, ArgumentError, code=ArgumentCodes.NOT_INT)
        assertion.assert_is_positiv(dimension, ArgumentError, code=ArgumentCodes.NOT_POSITIV)
        assertion.assert_not_zero(dimension, ArgumentError, code=ArgumentCodes.ZERO)
        d: list = list()
        if coordinates is None:
            coordinates: list = [0 for _ in range(dimension)]
        if isinstance(coordinates, tuple):
            coordinates = list(coordinates)
        assertion.assert_types(coordinates, TypesTuple.LISTS.value, ArgumentError,
                               code=ArgumentCodes.NOT_LISTS)
        for coord in coordinates:
            if isinstance(coord, TypesTuple.NUMBER.value):
                d.append([coord])
            elif isinstance(coord, TypesTuple.LISTS.value):
                d.append([coord[0]])
            else:
                raise ArgumentError(ArgumentCodes.UNEXPECTED_TYPE, wrong_argument=type(coord))
        super().__init__(d, dimension, 1)

    @classmethod
    def from_matrix(cls, matrix: Matrix) -> Self:
        assertion.assert_equals(matrix.get_rows(), 1, ArgumentError,
                                code=ArgumentCodes.MISMATCH_DIMENSION)
        coordinates: list = list()
        for component in matrix.get_components():
            coordinates.append(component[0])
        return Vector(coordinates, len(coordinates))

    @override
    def get_dimension(self) -> int:
        return len(self._data)

    @override
    def get_component(self, index: Types.INT.value) -> float:
        assertion.assert_types(index, TypesTuple.INT.value, ArgumentError, code=ArgumentCodes.NOT_INT)
        assertion.assert_range(index, 0, self.get_dimension() - 1, ArgumentError,
                               code=ArgumentCodes.OUT_OF_RANGE)
        return float(self._data[index][0])

    @override
    def set_component(self, index: Types.INT.value, value: Types.NUMBER.value) -> None:
        super().set_component(index, 1, value)

    def set_data(self, new: Types.LISTS.value) -> None:
        assertion.assert_types(new, TypesTuple.LISTS.value, ArgumentError,
                               code=ArgumentCodes.NOT_LISTS)
        assertion.assert_types_list(new, TypesTuple.NUMBER.value, ArgumentError, code=ArgumentCodes.NOT_NUMBER)
        new: list = list(new)
        to_data: list = list()
        for a in new:
            to_data.append([a])
        self._data = np.array(to_data)

    def get_data(self) -> np.ndarray:
        n: np.ndarray = self.get_components()
        n.reshape(self.get_dimension())
        return n

    def length(self) -> float:
        total: float = 0
        for entry in self._data:
            total += entry[0] * entry[0]
        return rnd(total ** (1/2))

    @override
    def __add__(self, other: Matrix) -> Self:
        added: Matrix = super().__add__(other)
        return Vector.from_matrix(added)

    @override
    def __radd__(self, other: Matrix) -> Self:
        added: Matrix = super().__radd__(other)
        return Vector.from_matrix(added)

    @override
    def __sub__(self, other: Matrix) -> Self:
        sub: Matrix = super().__sub__(other)
        return Vector.from_matrix(sub)

    @override
    def __rsub__(self, other: Matrix) -> Self:
        sub: Matrix = super().__rsub__(other)
        return Vector.from_matrix(sub)

    @override
    def __mul__(self, other: Union[Self, *TypesTuple.NUMBER.value]) -> Union[Self, float]:
        assertion.assert_types(other, (Vector, *TypesTuple.NUMBER.value), MathError, code=MathCodes.NOT_VECTOR_NUMBER)
        if isinstance(other, Vector):
            assertion.assert_equals(self.get_dimension(), other.get_dimension(), MathError,
                                    code=MathCodes.UNFIT_DIMENSIONS)
            a: np.ndarray = self.get_components()
            b: np.ndarray = other.get_components()
            c: np.ndarray = a * b
            d: float | int = 0
            if len(c) > 0 and isinstance(c[0], TypesTuple.LISTS.value):
                for sub in c:
                    d += sub[0]
            elif len(c) > 0 and isinstance(c[0], TypesTuple.NUMBER.value):
                print(c)
                for n in c:
                    d += n
            return rnd(d)
        vector: np.ndarray = self.get_data()
        return Vector(list(vector * other), self.get_dimension())

    @override
    def __rmul__(self, other: Union[Matrix, Self, *TypesTuple.NUMBER.value]) -> Self:
        if isinstance(other, (Vector, *TypesTuple.NUMBER.value)):
            return self * other
        multiple: Matrix = super().__rmul__(other)
        return Vector.from_matrix(multiple)

    @override
    def __imul__(self, other: Union[Matrix, *TypesTuple.NUMBER.value]) -> Self:
        if isinstance(other, Vector):
            raise MathError(MathCodes.VECTOR)
        return super().__imul__(other)

    @override
    def __truediv__(self, other: Types.NUMBER.value) -> Self:
        div: Matrix = super().__truediv__(other)
        return Vector.from_matrix(div)

    @override
    def __pow__(self, power, modulo=None):
        raise MathError(MathCodes.NOT_DEFINED, msg="This Action is not defined.")

    @override
    def __str__(self) -> str:
        return f"{self.get_data()}"

    @override
    def __repr__(self) -> str:
        return f"Vector at {hex(id(self))} with:\n {self.get_data()}"

    @override
    def copy(self) -> Self:
        return Vector.from_matrix(super().copy())
