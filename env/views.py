from flask import Flask, render_template, blueprints, request
import utils
import yagmail


main = blueprints.Blueprint('main', __name__)

#login
@main.route('/',methods=['GET','POST'])
def index():
 return render_template("login.html")

#registro paciente
@main.route('/registroPaciente/',methods=['GET','POST'])          
def registro():
    return render_template("pacientes/registroPaciente.html")



# ADMINISTRADOR
#home
@main.route('/inicio/')
def inicio():
    return render_template('administrador/inicioAdmin.html')

#crear cita
@main.route('/crearCita/',methods=['POST','GET'])
def CrearCita():
    return render_template('administrador/citas/nuevaCita.html')  

#gestion cita
@main.route('/gestioncita/',methods=['GET','POST','DELETE','PUT'])
def gestionCita():
    return render_template('administrador/citas/gestionarCitas.html')

#registro de usuarios
@main.route('/registroUsuario/')
def registroUsuario():
    return render_template('administrador/usuarios/registroUsuario.html')

#listado de pacientes
@main.route('/listadoPacientes/')
def listadoPacientes():
    return render_template('administrador/usuarios/listadoPacientes.html')

#listado de Medicos
@main.route('/listadoMedicos/')
def listadoMedicos():
    return render_template('administrador/usuarios/listadoMedicos.html')

#dashboard
@main.route('/dashboard/',methods=['GET'])
def dashboard():
    return render_template('administrador/dashboard.html')

@main.route('/perfil/')
def perfil():
    return render_template('perfilUsuario.html',)


