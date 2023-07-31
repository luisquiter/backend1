from flask import Flask, render_template
from profile import Profile
from firebase import FirebaseAdmin

app = Flask(__name__)

fb = FirebaseAdmin()

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/proyectos')
def proyectos():
    lista_proyectos = fb.get_collection('proy1')
    context = {
        'proyectos':lista_proyectos
    }
    return render_template('proyectos.html',**context)

@app.route('/resumen')
def resumen():
    experiencia_fb = fb.get_collection('experiencia')
    perfil_det = experiencia_fb[0]
    context = {
        'resumen':perfil_det['resumen'],
        'experiencia':perfil_det['laboral'],
        'descripcion':perfil_det['descripcion']
    }
    return render_template('resumen.html',**context)


@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


app.run(debug=True)
