import numpy as np

from useful_utility.errors import ArgumentError, MathError, ArgumentCodes, assertion, MathCodes
from useful_utility.algebra.statics import rnd


class Matrix:
    def __init__(self, columns: int = 2, rows: int = 2, data: list = None):
        if data is None:
            data = [[]]
        assertion.assert_type(rows, int, ArgumentError, code=ArgumentCodes.NOT_INT)
        assertion.assert_type(columns, int, ArgumentError, code=ArgumentCodes.NOT_INT)
        assertion.assert_types(data, (list, np.ndarray), ArgumentError, code=ArgumentCodes.NOT_LIST_NP_ARRAY)
        assertion.assert_is_positiv(rows, ArgumentError, code=ArgumentCodes.NOT_POSITIV)
        assertion.assert_is_positiv(columns, ArgumentError, code=ArgumentCodes.NOT_POSITIV)
        assertion.assert_not_zero(columns, ArgumentError, code=ArgumentCodes.ZERO)
        assertion.assert_not_zero(rows, ArgumentError, code=ArgumentCodes.ZERO)
        assertion.assert_layer_list(data, assertion.assert_types,
                                    {"types": (int, float, list)}, ArgumentError,
                                    code=ArgumentCodes.LIST_LAYER_NOT_INT_FLOAT_LIST)
        if len(data) > 0 and (isinstance(data[0], list) or isinstance(data[0], np.ndarray)):
            for d in data:
                assertion.assert_types(d, (list, np.ndarray), ArgumentError,
                                       code=ArgumentCodes.NOT_LIST_NP_ARRAY)
                assertion.assert_layer_list(d, assertion.assert_types,
                                            {"types": (int, float)}, ArgumentError,
                                            code=ArgumentCodes.LIST_LAYER_NOT_INT_FLOAT)

        self._rows: int = rows
        self._columns: int = columns
        self._data = np.array(data)
        if len(self._data) == 1 and len(data[0]) == 0:
            self._data = np.zeros(shape=(self._columns, self._rows))

    def get_rows(self) -> int:
        return self._rows

    def get_columns(self) -> int:
        return self._columns

    def get_component(self, column: int, row: int) -> float:
        assertion.assert_range(column, 0, len(self._data) - 1, ArgumentError, code=ArgumentCodes.OUT_OF_RANGE)
        assertion.assert_range(row, 0, len(self._data[column]) - 1, ArgumentError, code=ArgumentCodes.OUT_OF_RANGE)
        return float(self._data[column][row])

    def set_component(self, column: int, row: int, value: int | float | np.float64) -> None:
        assertion.assert_range(column, 0, len(self._data) - 1, ArgumentError, code=ArgumentCodes.OUT_OF_RANGE)
        assertion.assert_range(row, 0, len(self._data[column]) - 1, ArgumentError, code=ArgumentCodes.OUT_OF_RANGE)
        self._data[column][row] = value

    def get_components(self) -> np.ndarray:
        return self._data.copy()

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if self.get_rows() != other.get_rows() and self.get_columns() != other.get_columns():
                return False
            bools = self.get_components() == other.get_components()
            fin = list()
            for column in bools:
                fin.append(all(column))
            return all(fin)
        elif isinstance(other, np.ndarray):
            if self.get_components().shape != other.shape:
                return False
            bools = self.get_components() == other
            fin = list()
            for column in bools:
                fin.append(all(column))
            return all(fin)
        raise ArgumentError(ArgumentCodes.NOT_MATRIX_NP_ARRAY, msg="Only matrices or np.ndarray can be compared.", wrong_argument=type(other))

    def __add__(self, other) -> "Matrix":
        assertion.assert_type(other, Matrix, MathError, code=0, msg="Only a matrix can be added to a matrix.")
        if self.get_rows() != other.get_rows() or self.get_columns() != other.get_columns():
            raise MathError(MathCodes.UNFIT_DIMENSIONS, "The dimensions of the matrices do not fit!", other)
        matrixA = self.get_components()
        matrixB = other.get_components()
        return Matrix(self._columns, self._rows, data=list(matrixA + matrixB))
