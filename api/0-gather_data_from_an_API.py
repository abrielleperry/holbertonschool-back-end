#!/usr/bin/python3
""" given employee ID, returns infor about their TODO list progress"""
import requests
import sys


employee_user = requests.get("https://jsonplaceholder.typicode.com/users")
employee_todo = requests.get("https://jsonplaceholder.typicode.com/todos")

# print(employee_user.status_code)
# print(employee_user.json())

input_id = int(sys.argv[1])

name = None
for user in employee_user.json():
	if user['id'] == input_id:
		name = user['name']
		break
# print(name)

# completed = employee_todo.json()[0]['completed']
# print(completed)

true_count = {}
userid_count = {}

for todo_entry in employee_todo.json():
	userId = todo_entry['userId']
	completed = todo_entry['completed']

	if userId == input_id:
		userid_count[userId] = userid_count.get(userId, 0) + 1

	if completed:
		true_count[userId] = true_count.get(userId, 0) + 1

completed_tasks = true_count.get(input_id, 0)
total_tasks = userid_count.get(input_id, 0)


print(f"Employee {name} is done with tasks ({completed_tasks}/{total_tasks}):")


for todo_entry in employee_todo.json():
	title = 
