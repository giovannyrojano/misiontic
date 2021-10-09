from flask import Flask, render_template, blueprints, request
import utils
import yagmail


main = blueprints.Blueprint('main', __name__)

@main.route('/')
def index():
 return render_template("login.html")

@main.route('/cita/')
def cita():
    return render_template('citas/index.html')



@main.route('/dashboard/')
def dashboard():
    return render_template('dashboard/index.html')



@main.route('/listado/')
def listado():
    return render_template('pacientes/index.html',)

@main.route('/cita/',methods=['POST'])
def addCita():

    request.json["hora"]
    return render_template('cita/index.html')


@main.route('/registroUsuario',methods=['GET','POST'])          
def registro():
    return render_template("registroUsuario.html")

