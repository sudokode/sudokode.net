from flask import redirect

from sudokode_net import app

@app.route('/phpMyAdmin/scripts/setup.php')
@app.route('/myadmin/scripts/setup.php')
@app.route('/pma/scripts/setup.php')
@app.route('/wp-login.php')
@app.route('/login/')
@app.route('/admin/')
@app.route('/administrator/')
def hack():
    print("hacker alert!")
    return redirect("https://github.com/sudokode/sudokode.net")

