# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                   quickstart.15_about_responses.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# +---------------+
# | API with JSON |
# +---------------+

"""
A common response format when writing an API is JSON. It's easy to get started writing such an API with Flask. If you 
return a dict or list from a view, it will be converted to a JSON response.
"""

# +--------------------------------------------------------------------------------------------------------------------+
from flask import Flask
# +--------------------------------------------------------------------------------------------------------------------+

app = Flask(__name__)


@app.route('/me')
def me_api():
    return {
        "username": 'admin',
        "password": '0000'
    }


@app.route("/users")
def users_api():
    users = ['admin', 'root', 'user', 'guest']
    return [user for user in users]

"""
This is a shortcut to passing the data to the jsonify() function, which will serialize any supported JSON data type.
That means that all the data in the dict or list must be JSON serialize.

For complex types such as database models, you'll want to user a serialization library to convert the data to valid JSON
type first. There are many serialization libraries and Flask API extensions maintained by the community that support
more complex applications.
"""