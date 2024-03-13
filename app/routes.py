from . import app, db
from .models import Medico, Paciente, Consultorio, Cita
from flask import render_template, request, flash, redirect

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
@app.route("/medicos/create" , methods = ["GET" , "POST"] )
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
        flash("Medico Registrado Correctamente")
        return redirect("/medicos")
    
@app.route("/medicos/update/<int:id>", methods=["POST" , "GET"])
def update_medico(id):
    especialidades = [
            "Cardiologia", 
            "Pediatria", 
            "Oncologia", 
            "Ginecologia" 
        ]
    medico_update = Medico.query.get(id)
    if(request.method == "GET"):
        return render_template("medico_update.html", 
                           medico_update = medico_update,
                           especialidades = especialidades)
    elif(request.method == "POST"):
        ###### Actualizar el medico con los daros del form
        medico_update.nombres = request.form["nombres"]
        medico_update.apellidos = request.form["apellidos"]
        medico_update.tipo_identificacion = request.form["cc"]
        medico_update.numero_identificacion = request.form["nd"]
        medico_update.registro_medico = request.form["rm"]
        medico_update.especialidad = request.form["es"]

        db.session.commit()
        return "medico actualizado"

@app.route("/medicos/delete/<int:id>")
def delete_medico(id):
    medico_delete = Medico.query.get(id)
    db.session.delete(medico_delete)
    db.session.commit()
    return redirect("/medicos")


######## Crear ruta para crear nuevo paciente
    
@app.route("/pacientes/create" , methods = [ "GET" , "POST"] )
def create_paciente():
    if( request.method == "GET" ):
        return render_template("paciente_form.html")
    elif(request.method == "POST"):
        new_paciente = Paciente(nombres = request.form["nom"], 
                            apellidos = request.form["apell"],
                            tipo_identificacion = request.form["doc"],
                            numero_identificacion = request.form["numdoc"],
                            altura = request.form["est"],
                            tipo_sangre = request.form["ts"])   
         ######## añadir a la session sqlalchemy
        db.session.add(new_paciente)
        db.session.commit()
        flash("Paciente Registrado Correctamente")
        return redirect("/pacientes")



@app.route("/pacientes/update/<int:id>", methods=["POST" , "GET"])
def update_paciente(id):
    paciente_update = Paciente.query.get(id)
    if(request.method == "GET"):
        return render_template("paciente_update.html", 
                           paciente_update = paciente_update)
    elif(request.method == "POST"):
        ###### Actualizar el medico con los daros del form
        paciente_update.nombres = request.form["nom"]
        paciente_update.apellidos = request.form["apell"]
        paciente_update.tipo_identificacion = request.form["doc"]
        paciente_update.numero_identificacion = request.form["numdoc"]
        paciente_update.altura = request.form["est"]
        paciente_update.tipo_sangre = request.form["ts"]

        db.session.commit()
        return "paciente actualizado"

######## Crear ruta para crear nuevo con    sultorio
@app.route("/consultorios/create" , methods = [ "GET" , "POST"])
def create_consultorio():
    if( request.method == "GET" ):
        return render_template("consultorio_form.html")
    elif(request.method == "POST"):
        new_consultorio = Consultorio(numero = request.form["nc"])
        db.session.add(new_consultorio)
        db.session.commit()
        flash("Consultorio Registrado Correctamente")
        return redirect("/consultorios")
    