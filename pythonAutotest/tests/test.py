import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_subtracting_success(self):
        assert self.calc.subtraction(self,2, 1) == 1

    def test_subtracting_unsuccess(self):
        assert self.calc.subtraction(self, 1, 1) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)


    def teardown(self):
        print('Выполнение метода Teardown')
