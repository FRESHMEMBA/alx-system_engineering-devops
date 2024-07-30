#!/usr/bin/python3
import requests
from sys import argv

def get_data(id):
    """
    Given an employee ID, returns information about his/her TODO list progress
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.api.get(url=url)
    resources = response.json()

    for resource in resources:
        if resource.get("id") == id:
            return resource
    return {}

if __name__ == "__main__":
    id = argv[1]
    info = get_data(id=id)
    print(f"")