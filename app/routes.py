from . import app, db
from .models import Medico, Paciente, Consultorio, Cita
from flask import render_template, request

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

######## Crear ruta traer el medico por id (get)

@app.route("/medicos/<int:id>")
def get_medico_by_id(id):
    medico = Medico.query.get(id)
    return render_template("medico.html", med = medico)

######## Crear ruta traer el paciente por id (get)

@app.route("/pacientes/<int:id>")
def get_paciente_by_id(id):
    paciente = Paciente.query.get(id)
    return render_template("paciente.html", pac = paciente)

######## Crear ruta traer el consultorio por id (get)

@app.route("/consultorio/<int:id>")
def get_consultorio_by_id(id):
    consultorio = Consultorio.query.get(id)
    return render_template("consultorio.html", con = consultorio)

######## Crear ruta para crear nuevo medico
@app.route("/medicos/create" , methods = [ "GET" , "POST"] )
def create_medico():
    ######### Mostrar en el formulario: metodo get
    if( request.method == "GET" ):
        ##### El usuario ingreso con navegador con https://localhost:5000/medicos/create
        especialidades = ["Cardiologia", "Pediatria", "Oncologia", "Ginecologia"]
        return render_template("medico_form.html", especialidades = especialidades)

    ####### 2do momento, cuando el usuario presiona el boton de guardar
    ###### Sucede que los datos viajan al servidor utilizando post
    elif(request.method == "POST"):
        ###### Cuando se presiona "guardar"
        ###### Crear un objeto tipo medico
        new_medico = Medico(nombres = request.form["nombres"], 
                            apellidos = request.form["apellidos"],
                            tipo_identificacion = request.form["cc"],
                            numero_identificacion = request.form["nd"],
                            registro_medico = request.form["rm"],
                            especialidad = request.form["es"])
    ######## añadir a la session sqlalchemy
        db.session.add(new_medico)
        db.session.commit()
        return 'medico registrado'
######## Crear ruta para crear nuevo paciente
    
@app.route("/pacientes/create")
def create_paciente():
    return render_template("paciente_form.html")

######## Crear ruta para crear nuevo consultorio
@app.route("/consultorios/create")
def create_consultorio():
    return render_template("consultorio_form.html")
