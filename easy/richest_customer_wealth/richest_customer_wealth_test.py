from easy.richest_customer_wealth.richest_customer_wealth import RichestCustomerWealth
from utils.runner import run_solution


def test_richest_customer_wealth() -> None:
    task1672 = RichestCustomerWealth()
    run_solution(task1672, [
        [[1, 2, 3], [3, 2, 1]],
        [[1, 5], [7, 3], [3, 5]],
        [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
    ])
