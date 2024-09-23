def foo():
    raise OverflowError


try:
    foo()
except (AssertionError, ZeroDivisionError, ArithmeticError) as e:
    print(e.__class__.mro()[e.__class__ not in (AssertionError, ZeroDivisionError, ArithmeticError)].__name__)