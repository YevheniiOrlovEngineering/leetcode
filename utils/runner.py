from tabulate import tabulate
from utils.task import Task
from typing import Any


def run_solution(task_obj: Task, inputs: Any) -> None:
    diff_level = task_obj.__module__.split('.')[0]
    task_num = task_obj.task_num
    description = task_obj.__doc__
    outputs = [task_obj.solve(case) for case in inputs]

    data = [[diff_level, task_num, description, inputs, outputs]]
    headers = ["Difficulty level", "Task #", "Description", "Inputs", "Outputs"]

    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
