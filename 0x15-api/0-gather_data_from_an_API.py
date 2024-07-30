#!/usr/bin/python3
"""
For a given employee ID, information about
    his/her TODO list progress is returned.

Uses the requests module to connect to the API
The script accepts an integer as a parameter, which is the employee ID
The script displays on the standard output the employee TODO
list progress in this exact format:
First line: Employee EMPLOYEE_NAME is done with tasks(DONE/TOTAL):
EMPLOYEE_NAME: name of the employee
DONE: number of completed tasks
TOTAL: total number of tasks, which is the sum of
    completed and non-completed tasks
The second and N next lines display the title of completed tasks:
TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""

from my_tools import get_employee_info
from sys import argv

if __name__ == "__main__":
    employee_id = int(argv[1])
    employee_name, todos = get_employee_info(employee_id)
    completed_tasks = [todo for todo in todos if todo.get("completed")]
    number_of_complete_tasks = len(completed_tasks)
    total_tasks = len(todos)

    format = f"{number_of_complete_tasks}/{total_tasks}:"
    print(f"Employee {employee_name} is done with tasks"+format)

    for task in completed_tasks:
        print(f"\t {task.get('title')}")
