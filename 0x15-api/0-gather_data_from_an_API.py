#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress
from the JSONPlaceholder REST API.
"""

import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    b_url = 'https://jsonplaceholder.typicode.com'

    response_users = requests.get(f'{b_url}/users/{employee_id}').json()
    name = response_users["name"]

    resp_todo = requests.get(f'{b_url}/todos?userId={employee_id}').json()
    todo = len(resp_todo)
    todo_d = sum(1 for task in resp_todo if task["completed"])

    print("Employee {} is done with tasks({}/{}):".format(name, todo_d, todo))
    for task in resp_todo:
        if task["completed"]:
            print(f"\t {task['title']}")
