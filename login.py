from flask import Blueprint, request, jsonify

login = Blueprint('login', __name__)



@login.route('/login', methods=['POST'])
def llamarServicioSet():
    global user,passw

    user =request.json['user']
    passw =request.json['passw']

    print("Username",user)
    print("Password",passw)
    