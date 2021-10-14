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

#perfil
@main.route('/perfil/',methods=['GET','POST','PUT'])
def perfil():
    return render_template('perfil.html',)


