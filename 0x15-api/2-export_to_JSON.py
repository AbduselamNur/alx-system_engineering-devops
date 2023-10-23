#!/usr/bin/python3
""" Module Gather data from an API
    And Export to csv file
"""
import json
import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/"
    emp_url = url + emp_id
    todo_url = emp_url + "/todos"

    emp_res = requests.get(emp_url).json()
    todo_res = requests.get(todo_url).json()
    emp_name = emp_res.get('name')
    file_name = emp_id + ".json"
    data = {emp_id: []}
    for todo in todo_res:
        data[emp_id].append({
            "task": todo.get('title'),
            "completed": todo.get("completed"),
            "username": emp_res.get('username')})
    with open(file_name, mode='w') as f:
        json.dump(data, f)
