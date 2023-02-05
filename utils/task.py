from typing import Any


class Task:
    __task_num = None

    def solve(self, testcase: Any):
        pass

    @property
    def task_num(self) -> int:
        return self.__task_num
