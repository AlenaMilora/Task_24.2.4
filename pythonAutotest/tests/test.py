import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_subtracting_success(self):
        assert self.calc.subtraction(self,2, 1) == 1
        'проверяем метод калькулятора - вычитание'

    def test_multiplying_success(self):
        assert self.calc.multiply(self,5, 10) == 50
        'проверяем метод калькулятора - умножение'

    def test_division_success(self):
        assert self.calc.division(self,5, 10) == 0.5
        'проверяем метод калькулятора - деления'

    def teardown(self):
        print('Выполнение метода Teardown')
