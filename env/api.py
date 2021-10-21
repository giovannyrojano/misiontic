from flask import jsonify, blueprints
from db import get_db
from flask.globals import request
import sqlite3
from datetime import datetime

from werkzeug.security import check_password_hash, generate_password_hash

api = blueprints.Blueprint('api', __name__)


@api.route('/TipoDocumento/')
def getTipoDocumento():
    db = get_db()
    db.row_factory = sqlite3.Row
    filas = db.execute("SELECT * FROM tipo_documento").fetchall()

    db.close()
    mensajes = []
    for item in filas:
        mensajes.append({k: item[k] for k in item.keys()})
    return jsonify(mensajes)


@api.route('/paciente/', methods=['POST'])
def saveUsuario():
    try:
        db = get_db()
        {
            "apellidos": "231",
            "telefono": "12312",
            "direccion": "123",
            "documento": "12312",
            "documento_id": "1",
            "nombres": "1231",
            "password": "1234"
        }

        apellidos = request.json['apellidos']
        celular = request.json['telefono']
        direccion = request.json['direccion']
        documento = request.json['documento']
        tipo_documento_id = request.json['documento_id']
        password = request.json['password']
        nombres = request.json['nombres']
        # encriptar la contraseña
        clave = password + documento
        clave = generate_password_hash(clave)
        fecha = datetime.now()

        fila = db.execute("SELECT * FROM usuario where documento=? and tipo_documento_id=? ",
                          (documento, tipo_documento_id)).fetchall()
        if(len(fila) > 0):
            return jsonify({"error": True, "msg": "ya esta registrado este paciente"})

        db.execute(
            "insert into usuario (rol_id,apellidos,telefono,direccion,documento,tipo_documento_id, password,nombres,created_at,updated_at) values(?,?,?,?,?,?,?,?,?,?)",
            ([1, apellidos, celular, direccion, documento, tipo_documento_id, clave, nombres, fecha, fecha]))
        db.commit()
        db.close()
    # atrapar si existe algun error
    except sqlite3.Error as error:
        return jsonify({"error": True, "msg": error})
    return jsonify({"error": False, "msg": "creado correctamente"})


@api.route('/registrar/paciente')
def registrarPaciente():

    nombre = request.json['nombre']
    return jsonify(mensajes)


@api.route('/test/')
def mensaje():
    mensajes="ok"
    return jsonify(mensajes)