from flask import Flask, render_template, blueprints, request
import utils
import yagmail


main = blueprints.Blueprint('main', __name__)

@main.route('/')
def index():
 return render_template("index.html")

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




@main.route('/registro', methods=['GET', 'POST'])
def registro():

    if(request.method == 'POST'):

        correoUsuario=request.form['correo']
        nombreUsuario=request.form['nombre']
        claveUsuario=request.form['userPassword']

        cad="Hola {0}, este es un correo de pruba.".format(nombreUsuario)
        #Esto es solo una demo, Esto es seguro
        try:
            clienteMail = yagmail.SMTP("tucuentdeCorreo@gmail.com","1234ABC")
            clienteMail.send(to=correoUsuario, subject="Activa tu cuenta", contents=cad )
        except BaseException as e:
            return "Error" + str(e)


        return render_template("login.html")


    return render_template("registro.html")