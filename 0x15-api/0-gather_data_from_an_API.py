#!/usr/bin/python3
import requests
from sys import argv

def get_employee_info(id):
    """
    Given an employee ID, returns information about his/her TODO list progress
    """
    users_url = f"https://jsonplaceholder.typicode.com/users/{id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={id}"

    users_response = requests.get(url=users_url)
    todos_response = requests.get(url=todos_url)

    if users_response.status_code != 200:
        return None, []
    
    employee_name = users_response.json().get("name")

    if todos_response.status_code != 200:
        return employee_name, []
    
    todos = todos_response.json()

    return employee_name, todos

if __name__ == "__main__":
    id = argv[1]
    employee_name, todos = get_employee_info(id=id)
    completed_tasks = [todo for todo in todos if todo.get("completed")]
    number_of_complete_tasks = len(completed_tasks)
    total_tasks = len(todos)
    print(f"Employee {employee_name} is done with tasks({number_of_complete_tasks}/{total_tasks})")

    for task in completed_tasks:
        print(f"\t {task.get('title')}")