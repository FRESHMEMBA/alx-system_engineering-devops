import requests

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