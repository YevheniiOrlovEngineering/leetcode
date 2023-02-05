from utils.task import Task


class NumberOfStepsToReduceNumberToZero(Task):
    """
Given an integer num, return the number of steps to reduce it to zero.
In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
    """
    task_num = 1342

    def solve(self, num: int) -> int:
        cnt = 0
        while num != 0:
            if num % 2:
                num -= 1
            else:
                num /= 2
            cnt += 1
        return cnt

    def solve_optimal(self, num: int) -> int:
        return self.solve(num)
