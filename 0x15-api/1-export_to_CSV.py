#!/usr/bin/python3
"""
This Script exports data in the CSV format.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    emp_id = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/'

    user_resp = requests.get(f'{url}users/{emp_id}').json()
    user_id = user_resp.get('id')
    username = user_resp.get('username')

    todo_resp = requests.get(f'{url}todos?userId={emp_id}').json()

    csv_data = []
    for todo in todo_resp:
        task_completed_status = "True" if todo.get('completed') else "False"
        task_title = todo.get('title')
        csv_data.append([user_id, username, task_completed_status, task_title])

    csv_filename = ("{}.csv".format(user_id))
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)
