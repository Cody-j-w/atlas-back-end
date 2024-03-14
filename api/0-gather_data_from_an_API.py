#!/usr/bin/python3

"""
Module defining an API retrieval script
"""

import requests
import sys

if __name__ == '__main__':

    base_url = 'https://jsonplaceholder.typicode.com/'
    user_ext = '/users/{}'.format(sys.argv[1])
    todo_ext = '/todos'

    employee_response = requests.get(base_url+user_ext)
    employee = employee_response.json()
    todo_response = requests.get(base_url+user_ext+todo_ext)
    todos = todo_response.json()
    completed = 0
    total = 0
    for todo in todos:
        total += 1
        if todo['completed'] is True:
            completed += 1

    print("Employee {0} is done with tasks({1}/{2}):".format(
        employee['name'], completed, total
        ))
    for todo in todos:
        if todo['completed'] is True:
            print("\t {}".format(todo['title']))
