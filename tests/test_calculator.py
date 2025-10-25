import pytest
from src.calcuator import Calculator


class TestCalculator:
    
    @pytest.fixture
    def calc(self):
        return Calculator()
    
    def test_add(self, calc):
        assert calc.add(2, 3) == 5
        assert calc.add(-1, 1) == 0
        assert calc.add(0, 0) == 0
    
    def test_subtract(self, calc):
        assert calc.subtract(10, 5) == 5
        assert calc.subtract(0, 5) == -5
        assert calc.subtract(5, 5) == 0
    
    def test_multiply(self, calc):
        assert calc.multiply(3, 4) == 12
        assert calc.multiply(-2, 3) == -6
        assert calc.multiply(0, 100) == 0
    
    def test_divide(self, calc):
        assert calc.divide(10, 2) == 5
        assert calc.divide(9, 3) == 3
        assert calc.divide(7, 2) == 3.5
    
    def test_divide_by_zero(self, calc):
        with pytest.raises(ValueError, match="No se puede dividir por cero"):
            calc.divide(10, 0)
    
    def test_power(self, calc):
        assert calc.power(2, 3) == 8
        assert calc.power(5, 2) == 25
        assert calc.power(10, 0) == 1
    
    @pytest.mark.parametrize("a,b,expected", [
        (1, 1, 2),
        (5, 5, 10),
        (100, 50, 150),
        (-10, 10, 0),
    ])
    def test_add_parametrized(self, calc, a, b, expected):
        assert calc.add(a, b) == expected