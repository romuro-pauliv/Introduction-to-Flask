# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                    quickstart.12_request_object.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# +----------------+
# | Request Object |
# +----------------+

"""
The request object is documented in the API section and we will not cover it here in detail (see Request). Here is a 
broad overview of some of the most common operations. First fo all you have to import it from the flask module:

from flask import request

The current request method is available by using the method attribute. To access form data (data transmitted in a POST
or PUT request) you can use the form attribute. Here is a full example of the two attributes mentioned above:
"""

# +--------------------------------------------------------------------------------------------------------------------|
from flask import Flask, request, render_template
# +--------------------------------------------------------------------------------------------------------------------|

app = Flask(__name__)


def valid_login(username: str, password: str) -> bool:
    return True if username == 'admin' and password == '0000' else False


def log_the_user_in(username: str) -> str:
    return str(f"Welcome, {username}")


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            return 'Invalid username/password'
    return render_template('login.html', error=error)