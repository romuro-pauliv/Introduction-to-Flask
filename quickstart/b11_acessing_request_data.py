# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                            quickstart.11_accessing_request_data.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# +------------------------+
# | Accessing Request Data |
# +------------------------+

"""
For web applications it's crucial to react to the data a client sends to the server. In Flask this information is pro -
vided by the global request object. If you have some experience with Python you might be wondering how that object can 
be global and how Flask manages to still be threadsafe.

The answer is context locals:
"""

# +--------------+
# |Context Locals|
# +--------------+

"""
Insider Information:
    If you want to understand how that works and how you implement test with context locals, read this section otherwise
    just skip it

Certain objects in Flask are global objects, but not of the usual kind. These objects are actually proxies to objects
that are local to a specific context. What a mounthful. But that is actually quite easy to understand.

Imagine the context being the handling thread. A request comes in and the web server decides to spawn a new thread (or 
something else, the underlying object is capable of dealing with concurrency systems other than threads). When Flask 
starts its internal request handling it figures out that the current thread is the active context and binds the current 
application and the WSGI environments to that context (thread). It does that in an intelligent way so that one 
application con invoke another application without breaking.

So what does this mean to you? Basically you can completely ignore that this is the case unless you are doing something
like unit testing. You will notice that code which depends on a request object will suddenly break because there is no 
requests object. The solution is creating a request object yourself and binding it to the context. The easiest solution
for unit testing is ti use the test_request_context() context manager. In combination with the with statement it will
bind a test request so that you can interact with it. Here is an example:
"""

# +--------------------------------------------------------------------------------------------------------------------+
from flask import Flask, request
# +--------------------------------------------------------------------------------------------------------------------+

app = Flask(__name__)

@app.post("/hello")
def hello_post():
    return "POST METHOD"

with app.test_request_context('/hello', method='POST'):
    # now you can do somenthing with the request until the
    # end of the with block, such as basic assetions:
    assert request.path == '/hello'
    assert request.method == 'POST'

"""
The other possibility is passing a whole WSGI environment to the request_context() method:
"""

# with app.request_context():
#     assert request.method == 'POST'

"""
When you run this code a exception it will be displayed
TypeError: Flask.request_context() missing 1 required positional argument: 'environ'

inform at environ in request_context() function.
"""