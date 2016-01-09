from flask import render_template as temp

from sudokode_net import app

def passwd_temp():
    return temp('passwd.html', title="Password Checker")

@app.route('/passwd')
def passwd_index():
    return passwd_temp()

