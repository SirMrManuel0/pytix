from typing import Self
import numpy as np

from useful_utility.algebra.statics import rnd
from useful_utility.types import AllLists, Int, Number
from useful_utility.errors import assertion, ArgumentError, MathError, ArgumentCodes, MathCodes, TypesTuple, StateError

class Equation:
    """
    This is the base class for all equations. It is only meant to be inherited.

    C'est la classe de base pour toutes les équations. Elle dois être héritée.
    """
    def __init__(self, equation: str, parameters: AllLists) -> None:
        self._equation: str = ""
        self._parameters: list = list(parameters)

    def get_equation(self) -> str:
        return self._equation

    def get_parameters(self) -> list:
        return [*self._parameters]

    def copy(self) -> Self:
        return Equation(self._equation, self._parameters)

class Polynomial(Equation):
    """
    This class is the base class of polynomials.

    Cette classe est la classe de base des polynômes.
    """
    def __init__(self, degree: Int, parameters: AllLists, integrate_derive: bool = True) -> None:
        """
        :param degree: The highest power of the polynome.
        :rtype Int:
        :param parameters: All parameters of the polynome: a * x^2 + 0 * x + b -> [a, 0, b]
        :rtype AllLists:
        :param integrate_derive: Should the function be derived and integrated?
        :rtype bool:
        """
        assertion.assert_types(degree, TypesTuple.INT.value, ArgumentError, code=ArgumentCodes.NOT_INT)
        assertion.assert_types(parameters, (*TypesTuple.LISTS.value, *TypesTuple.TUPLE.value), ArgumentError,
                               code=ArgumentCodes.NOT_LISTS_TUPLE)
        assertion.assert_types_list(parameters, TypesTuple.NUMBER.value, ArgumentError, code=ArgumentCodes.NOT_NUMBER)
        assertion.assert_range(len(parameters), 1, degree + 1, ArgumentError, code=ArgumentCodes.OUT_OF_RANGE)
        assertion.assert_type(integrate_derive, bool, ArgumentError, code=ArgumentCodes.NOT_BOOl)

        while len(parameters) < degree + 1:
            parameters.append(0)

        super().__init__(self.generate_polynome(degree, parameters), parameters)
        self._degree: int = int(degree)
        self._integrale = self._integrate() if integrate_derive else None
        self._derivative_1 = self._derive() if integrate_derive else None
        self._derivative_2 = self._derive(2) if integrate_derive else None
        self._derivative_3 = self._derive(3) if integrate_derive else None

    @classmethod
    def generate_polynome(cls, degree: Int, parameters: AllLists) -> str:
        """
        Creates a string representation of the polynomial equation.

        Crée une chaîne de caractères de l'équation polynomiale.

        :param degree: The highest power of the polynome.
        :rtype Int:
        :param parameters: All parameters of the polynome: a * x^2 + 0 * x + b -> [a, 0, b]
        :rtype AllLists:
        :return: The string of the polynome.
        """
        equation: str = ""
        for power in range(degree, -1, -1):
            index: int = int(degree - power)
            if index == len(parameters):
                break
            if parameters[index] == 0:
                continue
            if power == 0:
                if not equation:
                    equation += f"{parameters[index]}"
                else:
                    equation += f" + {parameters[index]}"
                continue
            elif power == 1:
                if not equation:
                    equation += f"{parameters[index]} * x"
                else:
                    equation += f" + {parameters[index]} * x"
                continue

            if not equation:
                equation += f"{parameters[index]} * x**{power}"
            else:
                equation += f" + {parameters[index]} * x**{power}"
        return equation

    def get_degree(self) -> int:
        return self._degree

    def y_at_x(self, x: Number) -> float:
        assertion.assert_types(x, TypesTuple.NUMBER.value, ArgumentError, code=ArgumentCodes.NOT_NUMBER)
        y: float = 0
        for power in range(self._degree, -1, -1):
            index: int = int(self._degree - power)
            if index == len(self._parameters):
                break
            if self._parameters[index] == 0:
                continue
            y += rnd(self._parameters[index] * (x ** power))
        return y

    def area(self, start: Number, end: Number) -> float:
        assertion.assert_types(start, TypesTuple.NUMBER.value, ArgumentError, code=ArgumentCodes.NOT_NUMBER)
        assertion.assert_types(end, TypesTuple.NUMBER.value, ArgumentError, code=ArgumentCodes.NOT_NUMBER)
        assertion.assert_is_not_none(self._integrale, StateError, msg="The integral is not defined. If this should "
                                                                      "not be the case, use _integrate().")
        return rnd(self._integrale.y_at_x(end) - self._integrale.y_at_x(start))

    def get_roots(self, imaginary: bool = False) -> tuple:
        assertion.assert_type(imaginary, bool, ArgumentError, code=ArgumentCodes.NOT_BOOl)
        roots: list = list(np.roots(self._parameters))
        if not imaginary:
            roots: list = [r.real for r in roots if np.isreal(r)]
            roots: list = [rnd(root) for root in roots]
        return tuple(roots)

    def get_local_maximum(self) -> list[tuple[float, float]]:
        assertion.assert_is_not_none(self._derivative_1, StateError, msg="The first derivative is not defined. If "
                                                                         "this should not be the case, use _derive(1).")
        assertion.assert_is_not_none(self._derivative_2, StateError, msg="The second derivative is not defined. If "
                                                                         "this should not be the case, use _derive(2).")
        roots: tuple = self._derivative_1.get_roots()
        local_maximum: list = list()
        for root in roots:
            if self._derivative_2.y_at_x(root) < 0:
                local_maximum.append((root, self.y_at_x(root)))
        return local_maximum

    def get_local_minimum(self) -> list[tuple[float, float]]:
        assertion.assert_is_not_none(self._derivative_1, StateError, msg="The first derivative is not defined. If "
                                                                         "this should not be the case, use _derive(1).")
        assertion.assert_is_not_none(self._derivative_2, StateError, msg="The second derivative is not defined. If "
                                                                         "this should not be the case, use _derive(2).")
        roots: tuple = self._derivative_1.get_roots()
        local_minimum: list = list()
        for root in roots:
            if self._derivative_2.y_at_x(root) > 0:
                local_minimum.append((root, self.y_at_x(root)))
        return local_minimum

    def get_infliction_point(self) -> list[tuple[float, float]]:
        assertion.assert_is_not_none(self._derivative_2, StateError, msg="The second derivative is not defined. If "
                                                                         "this should not be the case, use _derive(2).")
        assertion.assert_is_not_none(self._derivative_3, StateError, msg="The third derivative is not defined. If "
                                                                         "this should not be the case, use _derive(3).")
        roots: tuple = self._derivative_2.get_roots()
        infliction_points = list()
        for root in roots:
            if self._derivative_3.y_at_x(root) != 0:
                infliction_points.append((root, self.y_at_x(root)))
        return infliction_points

    def limit_infinity(self, plus_inf: bool = True) -> int:
        assertion.assert_type(plus_inf, bool, ArgumentError, code=ArgumentCodes.NOT_BOOl)
        matters: float = float(self._parameters[0])
        if plus_inf:
            return 1 if matters > 0 else -1
        if self._degree % 2 == 0:
            return 1 if matters > 0 else -1
        return -1 if matters > 0 else 1

    def _integrate(self, amount: Int = 1) -> Self:
        integrated_parameters: list = list()
        integrated_degree: int = self._degree + 1
        for index, parameter in enumerate(self._parameters):
            if parameter == 0:
                continue
            integrated_parameters.append(rnd(parameter / (integrated_degree - index)))
        return Polynomial(integrated_degree, integrated_parameters, False)

    def _derive(self, amount: int = 1) -> Self:
        derived_parameters: list = list()
        derived_degree: int = self._degree - 1
        parameters: list = self.get_parameters()
        if len(self._parameters) == self._degree + 1:
            parameters: list = parameters[:-1]
        for index, parameter in enumerate(self._parameters):
            if parameter == 0:
                continue
            derived_parameters.append(rnd(parameter * (derived_degree - index)))
        return Polynomial(derived_degree, derived_parameters, False)



