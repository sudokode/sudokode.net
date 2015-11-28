from flask import Flask

app = Flask(__name__, static_folder='static')

import sudokode_net.views.robots
import sudokode_net.views.php
import sudokode_net.views.index
import sudokode_net.views.hello
