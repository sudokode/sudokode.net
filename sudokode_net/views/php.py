from flask import redirect

from sudokode_net import app

@app.route('/phpMyAdmin/scripts/setup.php')
@app.route('/myadmin/scripts/setup.php')
@app.route('/pma/scripts/setup.php')
def php():
    print("PHP lulz")
    return redirect("https://github.com/sudokode/sudokode.net")

