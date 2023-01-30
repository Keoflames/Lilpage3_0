from flask import Blueprint, request, jsonify

login = Blueprint('login', __name__)



@login.route('/login', methods=['POST'])
def llamarServicioSet():
    global user,password

    user =request.json['user']
    password =request.json['password']

    print("Username",user)
    print("Password",password)
    inicializarVariables(user,password)

    salida = {'codRes': codRes, 'menRes' : menRes, 'usuario':user,'accion':accion}
    return jsonify({'ParmOut' :salida})

def inicializarVariables(user,password):
    global codRes, menRes,accion
    userLocal="Sebastian"
    passLocal="1234"
    codRes = 'SIN_ERRROR'
    menRes = 'OK'
    try:
        print("Verificar login")
        if(str(password)==str(passLocal) and str (user)==str(userLocal)):
            print("Usuario y contraseña oK")
            accion="succes"
        else:
            print("Usuario o contraseña incorrecta")
            accion="usuario o contraeña incorrecta"
    except Exception as e:
        print("Error",str(e))
        codRes='ERROR'
        menRes='Msg'+str(e)
        