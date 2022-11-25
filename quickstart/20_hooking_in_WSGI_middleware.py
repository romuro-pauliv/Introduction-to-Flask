# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                        quickstart.20_hooking_in_WSGI_middleware.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# +----------------------------+
# | Hooking in WSGI Middleware |
# +----------------------------+

"""
To add WSGI middleware to your Flask application, wrap the application's wsgi_app attribute. For example, to apply 
Werkzeug's ProxyFix middleware for running behind Nginx:
"""

# +--------------------------------------------------------------------------------------------------------------------+
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
# +--------------------------------------------------------------------------------------------------------------------+

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

"""
Wrapping app.wsgi_app instead of app means that app sitll points at your Flask application, not at the middleware, so 
you can continue to use and configure app directly.
"""
