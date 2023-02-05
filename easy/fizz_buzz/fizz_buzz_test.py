from easy.fizz_buzz.fizz_buzz import FizzBuzz
from utils.runner import run_solution


def test_fizz_buzz() -> None:
    task412 = FizzBuzz()
    run_solution(task412, [3, 5, 15])
