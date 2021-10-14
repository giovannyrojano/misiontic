from flask import Flask, render_template, blueprints, request
import utils
import yagmail


main = blueprints.Blueprint('main', __name__)

#login
@main.route('/',methods=['GET','POST'])
def index():
 return render_template("login.html")

#registro
@main.route('/registroUsuario',methods=['GET','POST'])          
def registro():
    return render_template("registroUsuario.html")

#home
@main.route('/inicio/')
def inicio():
    return render_template('home/inicio.html')

#citas
@main.route('/gestioncita/',methods=['GET','POST','DELETE','PUT'])
def cita():
    return render_template('citas/gestionarCitas.html')


#crear cita
@main.route('/cita/create/',methods=['POST','GET'])
def CrearCita():
    return render_template('citas/crearCita.html')    

#dashboard
@main.route('/dashboard/',methods=['GET'])
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

@main.route('/cita/',methods=['PUT'])
def dropCita():
    #editar cita
    return render_template('cita/index.html')

@main.route('/cita/',methods=['DELETE'])
def dropCita():
    #eliminar cita
    return render_template('cita/index.html')



#medico
@main.route('/medico/',methods=['POST'])
def addMedico():
  #agregar medico
    return render_template('medico/index.html')

@main.route('/medico/',methods=['PUT'])
def editMedico():
    #editar medico
     return render_template('medico/index.html')

@main.route('/medico/',methods=['DELETE'])
def dropMedico():
    #eliminar medico
   return render_template('medico/index.html')



#administrador
@main.route('/administrador/',methods=['POST'])
def addAdministrador():
  #agregar administrador
    return render_template('administrador/index.html')

@main.route('/administrador/',methods=['PUT'])
def editAdministrador():
    #editar administrador
     return render_template('administrador/index.html')

@main.route('/administrador/',methods=['DELETE'])
def dropAdministrador():
    #eliminar administrador
   return render_template('administrador/index.html')



@main.route('/perfil/')
def perfil():
    return render_template('perfil.html',)


