import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_correct(self):
        assert self.calc.multiply(self, 2 ,2) == 4

    def test_division_correct(self):
        assert int(self.calc.division(self, 2 ,2)) == 1

    def test_subtraction_correct(self):
        assert self.calc.subtraction(self, 4 ,3) == 1

    def test_adding_correct(self):
        assert self.calc.adding(self, 2 ,2) == 4

