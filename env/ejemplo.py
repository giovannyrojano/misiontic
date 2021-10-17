
from db import get_db
from flask import jsonify, blueprints
from flask.globals import request
from markupsafe import escape

import sqlite3
ejemplo = blueprints.Blueprint('ejemplo', __name__)


@ejemplo.route('/getUno/')
def getUNo():
    # importar la bd
    db = get_db()
    # usar para que aparezcan las columnas
    db.row_factory = sqlite3.Row
    fila = db.execute("SELECT * FROM usuario").fetchall()
    mensajes = []
    # si tiene almenos 1 dato
    if(len(fila) > 0):
        # agregar con columnas
        for item in fila:
            mensajes.append({k: item[k] for k in item.keys()})
    db.close()
    # extraer el primero y unico
    return jsonify(mensajes[0])


# traer un  conjunto completo
@ ejemplo.route('/getMuchos/')
def getMuchos():

    db = get_db()
    db.row_factory = sqlite3.Row
    filas = db.execute("SELECT * FROM usuario").fetchall()

    db.close()
    mensajes = []
    for item in filas:
        mensajes.append({k: item[k] for k in item.keys()})
    return jsonify(mensajes)



# traer un  conjunto completo
@ ejemplo.route('/getMuchos/')
def saveUno():

    db = get_db()
    db.row_factory = sqlite3.Row
    filas = db.execute("SELECT * FROM usuario").fetchall()

    db.close()
    mensajes = []
    for item in filas:
        mensajes.append({k: item[k] for k in item.keys()})
    return jsonify(mensajes)




# almacenar en una tabla que los campos sean dinamicos
#no terminado
@ejemplo.route('/save/', methods=['POST'])
def save():
    # importar la bd
    db = get_db()
    data = request.json
    campos = []
    datos = []
    # se extraen las llaves
    for key in data.keys():
        campos.append(key)
    # se extraen los valores
    for val in data.values():
        datos.append(str(val))
    # se crea un separador
    coma = ","
    # se le agregar el separador al array
    info_campos = coma.join(campos)
    info_datos = coma.join(datos)
    print(info_campos)
    print(info_datos)

    sql = f'insert into usuario ({info_campos}) values({info_datos})'

    print(sql)

    return jsonify(sql)

    return keys
    usuario = escape(request.json['usuario'])
    asunto = escape(request.json['asunto'])
    mensaje = escape(request.json['mensaje'])
    db.execute("insert into mensajesV1 ( usuario, asunto, mensaje) values( ?, ?, ?)",
               (usuario, asunto, mensaje))
    db.commit()
    db.close()

    return jsonify(mensajes[0])
