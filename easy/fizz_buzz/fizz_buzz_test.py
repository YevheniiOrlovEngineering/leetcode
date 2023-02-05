from easy.fizz_buzz.fizz_buzz import FizzBuzz
from utils.runner import run_solution


def test_fizz_buzz() -> None:
    task1672 = FizzBuzz()
    run_solution(task1672, [3, 5, 15])
