from tabulate import tabulate
from utils.task import Task


def run_solution(task_obj: Task, inputs: list[str]) -> None:
    diff_level = task_obj.__module__.split('.')[0]
    task_num = task_obj.task_num
    description = task_obj.__doc__
    outputs = [str(task_obj.solve(case)) for case in inputs]

    data = [[diff_level, task_num, description, ", ".join(inputs), ", ".join(outputs)]]
    headers = ["Difficulty level", "Task #", "Description", "Inputs", "Outputs"]

    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
