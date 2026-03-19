import pytest

from mathutils import add, subtract, multiply, divide, factorial, fibonacci


class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -1) == -2

    def test_mixed_signs(self):
        assert add(-1, 1) == 0

    def test_floats(self):
        assert add(0.1, 0.2) == pytest.approx(0.3)


class TestSubtract:
    def test_positive_numbers(self):
        assert subtract(5, 3) == 2

    def test_result_negative(self):
        assert subtract(3, 5) == -2


class TestMultiply:
    def test_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_by_zero(self):
        assert multiply(5, 0) == 0

    def test_negative_numbers(self):
        assert multiply(-2, -3) == 6


class TestDivide:
    def test_even_division(self):
        assert divide(10, 2) == 5.0

    def test_float_result(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(1, 0)


class TestFactorial:
    def test_zero(self):
        assert factorial(0) == 1

    def test_one(self):
        assert factorial(1) == 1

    def test_five(self):
        assert factorial(5) == 120

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            factorial(-1)

    def test_float_raises(self):
        with pytest.raises(ValueError):
            factorial(2.5)


class TestFibonacci:
    def test_zero(self):
        assert fibonacci(0) == 0

    def test_one(self):
        assert fibonacci(1) == 1

    def test_ten(self):
        assert fibonacci(10) == 55

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            fibonacci(-1)
