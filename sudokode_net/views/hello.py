from flask import request, make_response, url_for, redirect, abort, render_template as temp

from sudokode_net import app, hello_feed

def hello_temp(name=None, save=False, erase=False):
    return make_response(temp('hello.html', title="Hello", name=name, save=save, erase=erase, hello_feed=hello_feed))

@app.route('/hello/', methods=['POST', 'GET'])
def hello_index():
    if request.method == 'POST':
        if request.form['name']:
            name = request.form['name']

            if request.form.get('save'):
                print("{} saved their name!".format(name))
                return redirect(url_for('hello_save', name=name))
            else:
                print("{} didn't save their name :(".format(name))
                return redirect(url_for('hello', name=name))
        return hello_temp()
    elif request.cookies.get('name'):
        return redirect(url_for('hello', name=request.cookies.get('name')))

    return hello_temp()

@app.route('/hello/<path:name>/')
def hello(name):
    if not name:
        abort(404)

    print("Hello from {}!".format(name))

    if request.cookies.get('name'):
        return hello_temp(request.cookies.get('name'), save=True)

    return hello_temp(name)

@app.route('/hello/<path:name>/save')
def hello_save(name):
    if not name:
        abort(403)

    response = hello_temp(name, save=True)
    response.set_cookie('name', name)

    if len(hello_feed) == 10:
        hello_feed.pop()
    hello_feed.append(name)

    print("{} saved their name!".format(name))

    return response

@app.route('/hello/<path:name>/erase')
def hello_erase(name):
    if not name:
        abort(404)

    if request.cookies.get('name'):
        response = hello_temp(erase=True)
        response.set_cookie('name', '', expires=0)
        print("{} erased their name :(".format(name))
    else:
        response = hello_temp()

    return response

