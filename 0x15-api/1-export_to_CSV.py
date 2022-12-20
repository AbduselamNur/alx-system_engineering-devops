#!/usr/bin/python3
""" Module Gather data from an API
    And Export to csv file
"""
import requests
import sys
import csv


if __name__ == "__main__":
    emp_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/"
    emp_url = url + emp_id
    todo_url = emp_url + "/todos"

    emp_res = requests.get(emp_url).json()
    todo_res = requests.get(todo_url).json()
    emp_name = emp_res.get('name')
    file_name = emp_id + ".csv"
    with open(file_name, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for todo in todo_res:
            writer.writerow([emp_id, emp_res.get('username'),
                            todo.get("completed"), todo.get("title")])
