from flask import Flask

app = Flask(__name__, static_folder='static')

hello_feed = list()

import sudokode_net.views.robots
import sudokode_net.views.php
import sudokode_net.views.chan4
import sudokode_net.views.index
import sudokode_net.views.hello
