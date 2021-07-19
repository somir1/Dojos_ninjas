from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def show_dojo():

    dojos = Dojo.show()
    return render_template("index.html", dojos = dojos)

@app.route('/dojos/<int:dojo_id>')
def show_dojos_with_id(dojo_id):

    ninjas = Ninja.get_ninjas_with_dojo_id(dojo_id)
    dojo = Dojo.dojo_with_id(dojo_id)

    return render_template("dojoshow.html", ninjas = ninjas, dojo = dojo )

@app.route('/makedojos', methods = ['POST'])
def make_dojo():
    
    dojo_id = Dojo.create_dojo(request.form)
    print(dojo_id)
    return redirect('/dojos')

@app.route('/ninja')
def make_ninja():
    dojos = Dojo.show()
    return render_template("makeninja.html", dojos = dojos)

@app.route('/createninja', methods = ['POST'])
def create_ninja():
    print("ninja is made")
    print(request.form)
    dojo_id = request.form['dojo_id']
    Ninja.create_ninja(request.form)
    return redirect("/dojos/"+ dojo_id)

