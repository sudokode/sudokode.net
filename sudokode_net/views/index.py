from flask import render_template as temp

from sudokode_net import app

@app.route('/')
def index():
    return temp('index.html', title="Soon")

@app.route('/halfwit/')
def halfwit():
    return 'Canadia!'

@app.route('/rookiearchadmin/')
def rookie():
    return 'I C U P'

@app.route('/meskarune/')
def meskarune():
    return "Yay it's meskarune!"

