# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                       quickstart.8_HTTP_methods.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# +--------------+
# | HTTP Methods |
# +--------------+

"""
Web application use differents HTTP methods when accessing URLs. You should familiarize yourself with the HTTP methods
as you work with Flask. By default, a route only answers to GET requests. You can use the methods arguments of the
route() decorator different HTTP methods.
"""

"""
You can use to Postman application to test GET and POST methods.
"""

# +--------------------------------------------------------------------------------------------------------------------|
from flask import Flask
from flask import request
# +--------------------------------------------------------------------------------------------------------------------|

app = Flask(__name__)


def do_the_login():
    return "POST METHOD"


def show_the_login_form():
    return "Login Page"

# V1.0 |---------------------------------------------------------------------------------------------------------------|
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
# |--------------------------------------------------------------------------------------------------------------------|

"""
The example above keeps all methods for the route within one function, which can be useful if each part uses some common
data.

You can also separate views for different methods into different functions. Flask provides a shortcut for decorating
such routes with get(), post(), etc. for each common HTTP method.
"""    

# V2.0 |---------------------------------------------------------------------------------------------------------------|
@app.get('/login')
def login_get():
    return show_the_login_form()

@app.get('/login')
def login_post():
    return do_the_login()
# |--------------------------------------------------------------------------------------------------------------------|

"""
if GET is present, Flask automatically adds support for the HEAD method and handles HEAD requests according to the HTTP
RFC. Likewise, OPTIONS is automatically implemented for you.
"""

