from flask import Flask, render_template, blueprints, request
import utils
import yagmail


main = blueprints.Blueprint('main', __name__)

#login
@main.route('/')
def index():
 return render_template("login.html")

#registro
@main.route('/registroUsuario',methods=['GET','POST'])          
def registro():
    return render_template("registroUsuario.html")




#citas
@main.route('/cita/')
def cita():
    return render_template('citas/gestionarCitas.html')

@main.route('/cita/create/')
def CrearCita():
    return render_template('citas/crearCita.html')    


#dashboard
@main.route('/dashboard/')
def dashboard():
    return render_template('dashboard/index.html')

#home
@main.route('/inicio/')
def inicio():
    return render_template('home/inicio.html')


@main.route('/listado/')
def listado():
    return render_template('pacientes/index.html',)


@main.route('/cita/',methods=['POST'])
def addCita():

    request.json["hora"]
    return render_template('cita/index.html')

@main.route('/perfil/')
def perfil():
    return render_template('perfil.html',)


