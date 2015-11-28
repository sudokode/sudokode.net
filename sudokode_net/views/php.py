from flask import render_template as temp

from sudokode_net import app

@app.route('/phpMyAdmin/scripts/setup.php')
@app.route('/myadmin/scripts/setup.php')
@app.route('/pma/scripts/setup.php')
def php():
    return 'PHP? Really? The source is <a href="https://github.com/sudokode/sudokode.net">here</a>.'

