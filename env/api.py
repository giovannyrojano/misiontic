from flask import jsonify, blueprints

api = blueprints.Blueprint('api',__name__)


@api.route('/test/')
def mensaje():
    mensajes="ok"
    return jsonify(mensajes)