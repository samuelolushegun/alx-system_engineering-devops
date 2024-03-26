import requests
import sys


def get_employee_todo_progress(employee_id):
    # Define base URL for JSONPlaceholder API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch user data
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    if user_response.status_code != 200:
        print(f"Failed to fetch user data for employee ID {employee_id}")
        return

    user_data = user_response.json()
    employee_name = user_data.get('name', 'Unknown')

    # Fetch todos for the given user
    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    if todos_response.status_code != 200:
        print(f"Failed to fetch todos for employee ID {employee_id}")
        return

    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    # Print employee todo progress
    print(f"Employee {employee_name} is done with tasks\
 ({completed_tasks}/{total_tasks}):")
    for todo in todos_data:
        if todo['completed']:
            print(f"\t{todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
