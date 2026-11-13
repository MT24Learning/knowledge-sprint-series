import math
import hypothesis as h
x = h.strategies.floats(0, 10)
@h.settings(derandomize=True)
@h.given(x, x, x)
def test_exact(a, b, c):
    assert (a+b)+c == a+(b+c)
@h.given(x, x, x)
def test_close(a, b, c):
    assert math.isclose((a+b)+c,
        a+(b+c), abs_tol=1e-9)
# pytest: 1 failed, 1 passed
# a=3.0338…, b=0.99999, c=1.0
