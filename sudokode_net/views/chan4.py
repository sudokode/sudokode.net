from flask import redirect

from sudokode_net import app

@app.route('/4chan/')
def chan4():
    print("4chan is here")
    return redirect("https://www.youtube.com/watch?v=DLzxrzFCyOs")

