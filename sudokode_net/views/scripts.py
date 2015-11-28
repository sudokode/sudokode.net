from flask import send_from_directory

from sudokode_net import app

@app.route('/js/<path:script>')
def scripts(script):
    return send_from_directory(app.static_folder, "js/{}".format(script))

@app.route('/css/<path:style>')
def styles(style):
    return send_from_directory(app.static_folder, "css/{}".format(style))

