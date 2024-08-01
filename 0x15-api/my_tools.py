#!/usr/bin/python3
import csv
import json
import requests

def get_employee_info(employee_id):
    """
    Given an employee ID, returns information about his/her TODO list progress
    """
    users_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    users_response = requests.get(url=users_url)
    todos_response = requests.get(url=todos_url)

    if users_response.status_code != 200:
        return None, []
    
    employee_name = users_response.json().get("name")

    if todos_response.status_code != 200:
        return employee_name, []
    
    todos = todos_response.json()

    return employee_name, todos


def export_to_csv(employee_id, employee_name, todos):
    """
    Exports data to CSV format
    """
    filename = f"{employee_id}.csv"
    with open(filename, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todos:
            writer.writerow([employee_id, employee_name, todo.get("completed"), todo.get("title")])


def export_to_json(employee_id, employee_name, todos):
    """
    Exports data to json
    """
    filename = f"{employee_id}.json"
    tasks = []
    json_obj = {}
    with open(filename, 'w') as file:
        for todo in todos:
            task_info = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": employee_name
            }
            tasks.append(task_info)
        
        data = {str(employee_id): tasks}

        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)
