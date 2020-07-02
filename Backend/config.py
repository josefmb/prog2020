from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
#Caminho do arquivo
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'time.db')
#Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Remover avisos
db = SQLAlchemy(app)