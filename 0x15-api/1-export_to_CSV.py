#!/usr/bin/python3

"""
Exports data in the CSV format.

Records all tasks that this employee owns
Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
The file name: USER_ID.csv
"""


from sys import argv
from my_tools import get_employee_info, export_to_csv


if __name__ == "__main__":
    employee_id = int(argv[1])
    employee_name, todos = get_employee_info(employee_id)
    export_to_csv(employee_id=employee_id, employee_name=employee_name, todos=todos)
