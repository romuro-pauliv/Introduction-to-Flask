### Application Setup

A Flask application is an instance of the **Flask** class. Everything about the application, such as configuration and URLs, will be registered with the class.

The most straightforward way to create a Flask application is to create a global **Flask** instance directly at the top of your code, like how the "Hello, World" example in [quickstart](). While this is sample and useful in some cases, it can cause some tricky issues as the project grows.

Instead of creating a **Flask** instance globally, you will create it inside a function. This function is known as the _aplication factory_. Any configuration, registration, and other setup the application needs will hapen inside the function, then the application will be returned.

----

#### The Application Factory

It's time to start coding! Create the `flaskr` directory and add the `__init__.py` file. The `__init__.py` server double duty: it will contain the application factory, and it tells Python that the `flaskr` directory should be treated as a package.

> flask/`__init__`.py

```Python
import os
from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
```

`create_app` is the application factory function. You'll add to it later in the tutorial, but it already does a lot.

1. `app = Flask(__name__, instance_relative_config=True)` creates the Flask instance
    + `__name__` is the name of the current Python module. The app needs to know where it's located to set up some paths, and `__name__` is a convenient way to tell it that.
    + `instance_relative_config=True` tells the app that configuration files are relative to the [instace folder](). The instance folder is located outside the `flaskr` package and can hold local data that shouldn't be commited to version control, such as configuration secrets and the database file.

2. **app.config.from_mapping( )** sets some default configuration that the app will use:
    + **SECRET_KEY** is used by Flask and extensions to keep data safe. It's set to `'dev'` to provide a convenient value during development, but it should be overriden with a random value when deploying.
3. 
