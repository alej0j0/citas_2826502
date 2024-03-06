from . import app
from .models import Medico, Paciente, Consultorio, Cita
from flask import render_template

##########  



########## Crear ruta para ver los medicos

@app.route("/medicos")
def get_all_medicos():
    medicos = Medico.query.all()
    return render_template("medicos.html" , medicos=medicos )

######### Creando ruta para pacientes 

@app.route("/pacientes")
def get_all_pacientes():
    pacientes = Paciente.query.all()
    return render_template("pacientes.html" , paciente=pacientes )

######## creando ruta para consultorios 
@app.route("/consultorios")
def get_all_consultorios():
    consultorios = Consultorio.query.all()
    return render_template("consultorios.html" , consultorios=consultorios)

###### Creando rutas para citas 

@app.route("/citas")
def get_all_citas():
    citas = Cita.query.all()
    return render_template("citas.html" , cita=citas)

