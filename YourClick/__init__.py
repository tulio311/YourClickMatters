import os 
import random

from flask import Flask, render_template


def create_app(test_config = None):
    #Create and configure the app
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE = os.path.join(app.instance_path,'flaskr.sqlite')
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def inicio():
        #colors = 0
        w = random.sample(["Hola","Marciano","Tinta","Agua","Quesadilla","Abstracto","Luz","Libro","Deuda"],4)
        return render_template('inicio.html', word1=w[0],word2=w[1],word3=w[2],word4=w[3])
    
    from . import db
    db.init_app(app)

    #from . import auth
    #app.register_blueprint(auth.bp)
    
    return app
