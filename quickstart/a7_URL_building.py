# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                       quickstart.7_URL_building.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# +--------------+
# | URL Building |
# +--------------+

"""
To build a URL to a specific function, use the url_for() function. It accepts the name of the function as its first 
argument and any number of keyword arguments, each corresponding to a variable part of the URL rule. Unknown variable 
parts are appended to the URL as query parameters.

Why would you want to build URLs using the URL reversing function url_for() instead of hard-coding them into your
templates?
"""

# (1)
"""
Reversing if often more descriptive than hard-conding the URLs
"""

# (2)
"""
Ypu can change your URLs in one go instead of needing to remember to manually change hard-coded URLs
"""

# (3)
"""
URL building handles escaping of especial characters transparently
"""

# (4)
"""
The generated paths are always absolute, avoiding unexpected behavior of relative paths in browsers
"""

# (5)
"""
If your application is placed outside the URL root, for example, in /myapplication instead of /url_for() properly
handles that for you
"""

"""
For example, here we use the test_request_context() method to try out url_for().
test_request_context() tells Flask to behave as though it's handling a request even while we use a Python shell.
See Context Locals: https://flask.palletsprojects.com/en/2.2.x/quickstart/#context-locals
"""

# +--------------------------------------------------------------------------------------------------------------------|
from flask import Flask
from flask import url_for
# +--------------------------------------------------------------------------------------------------------------------|

app = Flask(__name__)

@app.route("/")
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f"{username}\'s profile"

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Jonh Doe'))
