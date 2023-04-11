from flask import Flask, url_for, request, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from datetime import datetime
from turbo_flask import Turbo
import threading
import serial
from serial import SerialException
import time
import random
import re
import sys
import json
import numpy as np

app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
bootstrap = Bootstrap(app)
turbo = Turbo(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ser = serial.Serial('/dev/cu.usbmodem101', 9600, timeout=1) 
def read_arduino():
    print("I have entered read_arduino")
    while 1:
        try:
            data = ser.readline().decode("utf-8", errors="ignore")
            data = data.rstrip()
            return data
        except SerialException:
            time.sleep(0.01)
            continue
    return data

@app.context_processor
def inject_data():
    data = read_arduino()
    print(f"I have read the {data}")
    results = []
    if len(data)>2:
        split_data = data.split()
        if len(split_data)>1:
            bpm = data.split()[-2]
            comp_count = data.split()[-1]
            if not(bpm.isnumeric()): bpm='0'
        else:
            bpm = 0
            comp_count = split_data[0]
        results = [bpm, comp_count]
        print(results)
        return {'bpm': results[0], 'comp_count': results[1]}
    bpm = 0
    comp_count = 0
    results = [bpm, comp_count]
    print(results)
    return {'bpm': results[0], 'comp_count': results[1]}

def update_data():
    with app.app_context():
        while True:
            turbo.push(turbo.replace(render_template('loadbpm.html'), 'results'))

th = threading.Thread(target=update_data)
th.daemon = True
th.start()

from cprwalkthrough import routes, models