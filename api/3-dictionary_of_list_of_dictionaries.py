#!/usr/bin/python3
""" given employee ID, returns infor about their TODO list progress"""
import csv
import json
import requests
import sys


def get_employee():
    employee_user = requests.get("https://jsonplaceholder.typicode.com/users")
    employee_todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    return employee_user.json(), employee_todo.json()


# print(employee_user.status_code)
# print(employee_user.json())

if __name__ == "__main__":
    employee_user, employee_todo = get_employee()

    entiretasks = {}
    for user in employee_user:
        username = user['username']
        user_id = user['id']

        tasks = []

        for todo_entry in employee_todo:
            if todo_entry["userId"] == user_id:
                task = {
                    "task": todo_entry["title"],
                    "completed": todo_entry["completed"],
                    "username": username
                }
                tasks.append(task)

        entiretasks[str(user_id)] = tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(entiretasks, jsonfile)
    # print(name)

    # completed = employee_todo.json()[0]['completed']
    # print(completed)
    """
        true_count = {}
        userid_count = {}

        for todo_entry in employee_todo:
            userId = todo_entry['userId']
            completed = todo_entry['completed']

            if userId == input_id:
                userid_count[userId] = userid_count.get(userId, 0) + 1

            if completed:
                true_count[userId] = true_count.get(userId, 0) + 1

        completed_tasks = true_count.get(input_id, 0)
        total_tasks = userid_count.get(input_id, 0)

        print("Employee {} is done with tasks({}/{}):".format(
                                                                name,
                                                                completed_tasks,
                                                                total_tasks))

        for todo_entry in employee_todo:
            if todo_entry['userId'] == input_id and todo_entry['completed']:
                title = todo_entry['title']
                print("\t {}".format(title))
    """
