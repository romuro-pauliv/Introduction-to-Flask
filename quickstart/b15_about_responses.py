# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                   quickstart.15_about_responses.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# +------- ---------+
# | About Responses |
# +-----------------+

"""
The return value a view function is automatically converted into a reponse object for you. If the return value is a
string it's converted into a response object with the string as reponse body, a 200 OK status code and text/html 
mimetype. If the return value is a dict or lis, jsonify() is called to produce a response. The logic that Flask applies
to converting return values into reponse objects is a follows:
"""

# (1) - If a response object of the correct type is returned it's directly returned from the view.
# (2) - If it's a string, a response object is created with that data and the dafault parameters.
# (3) - If it's an iterator or generator returning string or bytes, it is treated as a streaming response.
# (4) - If it's dict or list, a response object is created using jsonify()
# (5) - If a tuple is returned the items in the tuple can provide extra information. Such tuples have to be in the form
#       (response, status), (response, headers), or (response, status, headers). The status value will override the 
#       status code and headers can be a list or dictionary of additional headers values.
# (6) - If none of that works, Flask will assume the return value is a valid WSGI application and convert that into a
#       response object.

"""
If you want to get hold of the resulting response object inside the view you can use the make_response() function

You need to wrap the return expression with make_response() and get the response object to modify it, then return it:
"""

# +--------------------------------------------------------------------------------------------------------------------+
from flask import Flask, render_template, make_response
# +--------------------------------------------------------------------------------------------------------------------+


app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('page_not_found.html'), 404)
    resp.headers['X-Something'] = 'A Value'
    return resp

