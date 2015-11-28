from flask import send_from_directory

from sudokode_net import app

@app.route('/robots.txt')
def robots():
    print('EEEK SPIIIIDDDEEEERRRRRSSSSS')
    return send_from_directory(app.static_folder, 'robots.txt')

