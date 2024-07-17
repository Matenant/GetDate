from flask import Flask, jsonify, request, Blueprint

test = Blueprint('test', __name__, template_folder='templates')

@test.route('/test')
def func_test():
    return 'Hello, tessssst'