from easy.number_of_steps_to_reduce_number_to_zero.number_of_steps_to_reduce_number_to_zero import NumberOfStepsToReduceNumberToZero
from utils.runner import run_solution


def test_number_of_steps_to_reduce_number_to_zero() -> None:
    task1342 = NumberOfStepsToReduceNumberToZero()
    run_solution(task1342, [14, 8, 123])
