# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                               quickstart.14_redirect_and_errors.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# +---------------------+
# | Redirect and Errors |
# +---------------------+

"""
To redirect a user to another endpoint, user the redirect() function; To abort a request early with an error code, use
the abort() function:
"""

# +--------------------------------------------------------------------------------------------------------------------|
from flask import abort, redirect, url_for, Flask, render_template
# +--------------------------------------------------------------------------------------------------------------------|


app = Flask(__name__)


def this_is_never_executed():
    return "OMG! Was this executed?" 


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()

"""
This is a rather pointless example because a user will be redirected from the index to a page they cannot access (401
means access denied) bit it shows how that works

By default a black and white error page is shown for each error code. If you want to customize the error page, you can
use the errorhandler() decorator:
"""

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

"""
Note the 404 after the render_template() call. This tell Flask that the status code of that page should be 404 which
means not found. By default 200 is assumed which translates to: all went well.
"""