from utils.runner import run_solution
from easy.roman_to_integer.roman_to_integer import RomanToInteger


def test_roman_to_integer() -> None:
    task13 = RomanToInteger()
    run_solution(task13, ["III", "LVIII", "MCMXCIV"])
