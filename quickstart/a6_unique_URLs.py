# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                        quickstart.6_unique_URLs.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# +----------------+
# | Variable Rules |
# +----------------+

# The following two rules differ in their use of a trailing slash.

# +--------------------------------------------------------------------------------------------------------------------|
from flask import Flask
# +--------------------------------------------------------------------------------------------------------------------|

app = Flask(__name__)

@app.route('/projects/')
def projects():
    return "The project page"

@app.route('/about')
def about():
    return "The about page"

# |--------------------------------------------------------------------------------------------------------------------|

"""
The canonical URL for the projects endpoint has a trailing slash. It's similar to a folder in a file system. If you 
access the URL without a trailing slash (/projects), Flask redirects to the canonical URL with the trailing slash ->
(/projects/)

The canonical URL for the about endpoint does not have a trailing slash. It's similar to the pathname of a file.
Accessing the URL with a trailing slash (/about/) produces a 404 "not found" error. This helps keep URLs unique for 
these resources, which helps search engines avoid indexing the same page twice.
"""
