from flask import request, redirect, render_template as temp

from sudokode_net import app

import passwordmeter as pwm

def passwd_temp(test=None):
    return temp('passwd.html', title="Password Checker", test=test)

@app.route('/passwd/')
def passwd_index():
    passwd = request.args.get('passwd', False)
    if passwd:
        return redirect('/passwd/' + passwd)
    return passwd_temp()

@app.route('/passwd/<path:passwd>')
def passwd_check(passwd=None):
    if passwd:
        test = pwm.test(passwd)
        return passwd_temp(test)
    else:
        return redirect('/passwd')

@app.context_processor
def utility_processor():
    def format_score(score):
        return "{0:.02f}%".format(score * 100)
    return dict(format_score=format_score)
