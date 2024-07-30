#!/usr/bin/python3
from my_tools import get_employee_info
from sys import argv

if __name__ == "__main__":
    id = int(argv[1])
    employee_name, todos = get_employee_info(id=id)
    completed_tasks = [todo for todo in todos if todo.get("completed")]
    number_of_complete_tasks = len(completed_tasks)
    total_tasks = len(todos)
    print(f"Employee {employee_name} is done with tasks({number_of_complete_tasks}/{total_tasks})")

    for task in completed_tasks:
        print(f"\t {task.get('title')}")