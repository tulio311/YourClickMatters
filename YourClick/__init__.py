import os 
import random
import json
import math
import pandas as pd

from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin


def getObj(data):
    result = {}
    for key_value_pair in data.split("&"):
        key, value = key_value_pair.split("=")
        result[key] = value

    with open('logs.txt', 'w') as file:
        file.writelines(json.dumps(result))
    
    return result


def create_app(test_config = None):
    #Create and configure the app
    app = Flask(__name__, instance_relative_config = True)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
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

    @app.route('/receive', methods=['POST'])
    @cross_origin()
    def guardar():
        dataB = db.get_db()
        #print(request.json())
        #color = request.json()
        data = request.get_data().decode('utf-8')
        dataObj = getObj(data)
        color = dataObj['color']
        word = dataObj['word']
        cur = dataB.cursor()
        cur.execute(f"INSERT INTO clicks (color,word) VALUES ('{color}','{word}');")
        dataB.commit()
        #data1 = json.loads(data)

        #with open('logs.txt', 'w') as file:
            #file.writelines(data)
        #    file.writelines(dataObj['color'] + dataObj['word'])




        return {'color': color, 'word': word, 'status':200}


    @app.route('/stats')
    def stats():
        dataB = db.get_db()
        cur = dataB.cursor()
        cur.execute("SELECT * FROM clicks;")
        X = cur.fetchall()

        #for row in X:
        #    with open('logs.txt', 'a') as file:
        #        file.writelines(str(row))

        totals = [0,0,0,0]
        perc = [0,0,0,0]
        totalsW = [0,0,0,0,0,0,0,0,0]
        percW = [0,0,0,0,0,0,0,0,0]
        words = ["Hola","Marciano","Tinta","Agua","Quesadilla","Abstracto","Luz","Libro","Deuda"]

        for i in range(len(X)):
            col = X[i][1]
            word = X[i][2]
            if col == 'Black':
                totals[0] += 1
            elif col == 'Blue':
                totals[1] += 1
            elif col == 'Green':
                totals[2] += 1
            elif col == 'Red':
                totals[3] += 1
            
            if word == 'Hola':
                totalsW[0] += 1
            elif word == 'Marciano':
                totalsW[1] += 1
            elif word == 'Tinta':
                totalsW[2] += 1
            elif word == 'Agua':
                totalsW[3] += 1
            elif word == 'Quesadilla':
                totalsW[4] += 1
            elif word == 'Abstracto':
                totalsW[5] += 1
            elif word == 'Luz':
                totalsW[6] += 1
            elif word == 'Libro':
                totalsW[7] += 1
            elif word == 'Deuda':
                totalsW[8] += 1


            

        for i in range(4):
            perc[i] = math.trunc(totals[i]*10000 / len(X))/100
        for i in range(9):
            percW[i] = math.trunc(totalsW[i]*10000 / len(X))/100

        #with open('logs.txt', 'a') as file:
        #    file.writelines(str(totals) + str(perc))

        return render_template('stats.html', totals = totals, perc = perc, totalsW = totalsW, percW = percW, words = words)



    

    #from . import auth
    #app.register_blueprint(auth.bp)
    
    return app
