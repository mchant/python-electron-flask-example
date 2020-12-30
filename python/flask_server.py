import sys 
import os 
from flask import Flask, render_template 
import platform
from flask_restx import Api, Resource, fields
from resources.todos.sample import Sample
from resources.system.computer import Computer
from flask_cors import CORS
  

if getattr(sys, 'frozen', False): 

    template_folder = os.path.join(sys._MEIPASS, 'templates') 
    static_folder = os.path.join(sys._MEIPASS, 'static') 

    print(template_folder) 
    print(static_folder) 

    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder) 

else: 

    app = Flask(__name__)


@app.route("/") 

def hello(): 

    return render_template("index.html") 

# allow api to be accessed from frontend
CORS(app)

# init api
api = Api(app, version='1.0', title='TodoMVC API',
    description='A simple TodoMVC API',
)

# init namespace
ns = api.namespace('todos', description='TODO operations')

# add routes
ns.add_resource(Sample, '/sample')
ns.add_resource(Computer, '/computer_name')

if __name__ == "__main__": 

    app.run(host='127.0.0.1', port=5000) 

