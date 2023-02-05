from utils.task import Task
from typing import List


class RichestCustomerWealth(Task):
    """You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the ith customer
has in the jth bank. Return the wealth that the richest customer has. A customer's wealth is the amount of
money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
    """
    task_num = 1672

    def solve(self, accounts: List[List[int]]):
        biggest_wealth = sum(accounts[0])

        for customer in accounts[1:]:
            current_wealth = sum(customer)
            if current_wealth > biggest_wealth:
                biggest_wealth = current_wealth

        return biggest_wealth

    def solve_optimal(self, accounts: List[List[int]]):
        return max(sum(account) for account in accounts)
