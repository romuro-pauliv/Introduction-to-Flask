# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                            quickstart.4_routing.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# +---------+
# | Routing |
# +---------+

"""
Modern web applications use meaningful URLs to help users. Users are more likely to like a page and come back if the pa-
ge uses a meaningful URL they can remember and use to directly visit a page.

Use the route() decorator to bind a function to a URL.
"""

# +--------------------------------------------------------------------------------------------------------------------|
from flask import Flask
# +--------------------------------------------------------------------------------------------------------------------|


app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page"

@app.route('/hello')
def hello():
    return "Hello, World!"

"""
You can do more! You can make parts of the URL dynamic and attach multiple rules to a function.
"""

