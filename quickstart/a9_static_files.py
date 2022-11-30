# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                       quickstart.9_static_files.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# +--------------+
# | Static Files |
# +--------------+

"""
Dynamic web applications also need static files. That's usually where the CSS and JavaScript files are coming from.
Ideally your web server is configured to serve them for you, but during development Flask can do that as well. Just 
create a folder called static in your package or next your module and it will be available at /static on the application

To generate URLs for static files, use the special 'static' endpoint name:
"""

# +--------------------------------------------------------------------------------------------------------------------+
from flask import Flask
from flask import url_for
# +--------------------------------------------------------------------------------------------------------------------+

app = Flask(__name__)


with app.test_request_context():
    print(url_for('static', filename='style.css'))

# The file has to be restored on the filesystem as static/style.css
