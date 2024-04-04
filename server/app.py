#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:str_to_print>')
def print_string(str_to_print):
    print(str_to_print)
    return f'{str_to_print}'

@app.route('/count/<int:int_to_count>')
def count(int_to_count):
    return "".join([f'{num}\n' for num in range(0, int_to_count)])

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    if operation == 'div':
        operation = '/'
    return f'{eval(f"{num1} {operation} {num2}")}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
