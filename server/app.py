#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views<h1>"

@app.route('/')
def print_string(parameter):
    print(parameter)
    return f'Printed: {parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    return "<br>".join([str(i) for i in range(parameter)])

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == 'add':
        result = num1 + num2
    elif operation == 'sub':
        result = num1 - num2
    elif operation == 'mul':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero!"
    elif operation == 'mod':
        result = num1 % num2
    else:
        return "Error: Invalid operation!"
    
    return f"The result of {num1} {operation} {num2} is {result}"
    


if __name__ == '__main__':
    app.run(port=5555, debug=True)

