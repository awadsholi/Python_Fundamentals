# Installing and managing dependencies with pip for install packages
#This example with installing the request package

import requests #for using api methods (CRUD)

response = requests.get("https://jsonplaceholder.typicode.com/todos/1") ## example of http get request and the response is in a json format

print(response) # this returns the status code of the response

print(response.json()) # returns the response in a json format