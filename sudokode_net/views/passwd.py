from flask import request, jsonify, render_template as temp

from sudokode_net import app

import passwordmeter as pwm

def passwd_temp(result=None):
    return temp('passwd.html', title="Password Checker", result=result)

def passwd_test(passwd):
    test = pwm.test(passwd)
    result = {
        'passwd': passwd,
        'score': test[0],
        'suggestions': test[1]
    }
    return result

@app.route('/passwd', methods=['GET', 'POST'])
@app.route('/passwd/<path:passwd>', methods=['GET', 'POST'])
def passwd_index(passwd=None):
    _passwd = request.args.get('passwd', False)

    if _passwd:
        result = passwd_test(_passwd)
        return passwd_temp(result)

    if passwd:
        result = passwd_test(passwd)
        return passwd_temp(result)

    if request.method == 'POST':
        passwd = request.form['passwd']

        if passwd:
            result = passwd_test(passwd)
            return jsonify(result)

    return passwd_temp()

@app.context_processor
def utility_processor():
    def format_score(score):
        return "{0:.02f}%".format(score * 100)
    return dict(format_score=format_score)

