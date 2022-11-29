# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                 flaskr.__init__.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# +-------------------+
# | Application Setup |
# +-------------------+

"""
A Flask application is an instance of the Flask class. Everything about the application, such as configuration and URLs,
will be registred with this class.

The most straghtforward way to create a Flask application is to create a global Flask instance directly at the top of 
your code, like how the "Hello, World". While this sample and useful in some cases, it can cause some tricky inssues as
the project grows.

Instead of creating a Flask instance globally, you will create it inside a function. This is function is known as the
application factory. Any configuration, registration, and other setup the application needs will happen inside the func-
tion, then application will be returned.
"""

# +-------------------------+
# | The Application Factory |
# +-------------------------+

"""
It's time to start coding! Create the flaskr directory and add the __init__.py file. The __init__.py server double duty:
it will contain the application factory, and it tells Python that the flaskr directory should be treated as a package.
"""

# +--------------------------------------------------------------------------------------------------------------------+
import os
from flask import Flask
# +--------------------------------------------------------------------------------------------------------------------+


def create_app(test_config: None = None) -> Flask:
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)
    
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that say hello
    @app.route('/hello')
    def hello() -> str:
        return 'Hello, World!'
    
    # After read db.py |-----------------------------------------------------------------------------------------------|
    from . import db
    db.init_app(app)
    # |----------------------------------------------------------------------------------------------------------------|
    
    return app

# (1) app = Flask(__name__, instance_relative_config=True) creates the Flask instace
"""
    - __name__ is the name of the current Python module. The app needs to know where it's located to set up some paths,
      and __name__ is a convenient way to tell it that.

    - Instance_relative_config=True tells the app that configuration files are relative to the instace folder. The ins -
      tance folder is located outside the flaskr package and can hold local data that shouldn't be commited to version
      control, such as configuration secrets and the database file.
"""

# (2) app.config.from_mapping() set some default configuration that the app will use:
"""
    - SECRET_KEY is used by Flask and extensions to keep data safe. It's set to 'dev' to provide a convenient value du -
      ring development, but it should be overridden with a random value when deploying.
    - DATABASE is the path where the SQLite database file will be saved. It's under app.instance.path, which is the path
      that Flask has chosen for the instance folder. You'll learn more about the database in the next section.
"""

# (3) app.config.from_pyfile
"""
    Overrides the default configuration with values taken from the config.py file in the instace folder if it exists. 
    For example, when deploying, this can be used to set a real SECRET_KEY.

    - test_config can also be passed to the factory, and will be used instead of the instance configuration. This is so
      the tests you'll write later in the tutorial can be configured independently of any development values you have 
      cofigured.
"""

# (4) os.makedirs()    
"""
    Ensures that app.instance.path exists. Flask doesn't create the instance folder automatically, but it needs to be
    created because your project will create the SQLite database file there.
"""

# (5) @app.route()
"""
    Creates a simple route so you can see the application working before getting into the rest of the tutorial. It
    creates a connection between the URL/hello and a function that returns a response, the string 'Hello, World' in this
    case.
"""

# +---------------------+
# | Run the Application |
# +---------------------+

"""
Now you can run your application using the flask command. From the terminal, tell Flask where to find your application,
then run it in debug mode. Remember, you should be in the top-level flask-tutorial directory, not the flaskr package.

Debug mode shows an interactive debugger whenever a page raises an exception, and restarts the server whenever you make
changes to the code. You can leave it running and just reload the browser page as you follow the tutorial.
"""

# $ flask --app flaskr --debug run

