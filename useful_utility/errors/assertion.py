
def assert_type(var, type_, exception, **kwargs) -> None:
    if not isinstance(var, type_):
        raise exception(**kwargs)


def assert_range(var, start, end, exception, **kwargs) -> None:
    if var < start or var > end:
        raise exception(**kwargs)


def assert_below(var, max_, exception, **kwargs) -> None:
    if var >= max_:
        raise exception(**kwargs)


def assert_above(var, min_, exception, **kwargs) -> None:
    if var <= min_:
        raise exception(**kwargs)


def assert_equals(var, equaled, exception, **kwargs) -> None:
    if var != equaled:
        raise exception(**kwargs)

def assert_type_list(var, type_, exception, **kwargs) -> None:
    if any([not isinstance(i, type_) for i in var]):
        raise exception(**kwargs)

def assert_is_positiv(var, exception, **kwargs) -> None:
    if var < 0:
        raise exception(**kwargs)

def assert_is_negative(var, exception, **kwargs) -> None:
    if var > 0:
        raise exception(**kwargs)

def assert_not_zero(var, exception, **kwargs) -> None:
    if var == 0:
        raise exception(**kwargs)

def assert_types(var, types: tuple, exception, **kwargs) -> None:
    check: list = list()
    for type_ in types:
        check.append(isinstance(var, type_))
    if not any(check):
        raise exception(**kwargs)

def assert_is_none(var, exception, **kwargs) -> None:
    if var is not None:
        raise exception(**kwargs)

def assert_is_not_none(var, exception, **kwargs) -> None:
    if var is None:
        raise exception(**kwargs)

def assert_layer_list(var, assert_, arg: dict, exception, **kwargs) -> None:
    for element in var:
        assert_(element, **arg, exception=exception, **kwargs)

def assert_false(var: bool, exception, **kwargs) -> None:
    if var:
        exception(**kwargs)

def assert_true(var: bool, exception, **kwargs) -> None:
    if not var:
        exception(**kwargs)

def assert_types_list(var, types: tuple, exception, **kwargs) -> None:
    for element in var:
        assert_types(element, types, exception, **kwargs)
