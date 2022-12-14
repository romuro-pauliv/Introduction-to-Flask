#### Summary
- [The Application Factory](https://github.com/romuro-pauliv/Introduction-to-Flask/blob/main/flask-tutorial/flaskr/md/init.md#the-application-factory)
- [Run the application](https://github.com/romuro-pauliv/Introduction-to-Flask/blob/main/flask-tutorial/flaskr/md/init.md#run-the-application)
----
### The Application Factory

It's time to start coding! Create the `flaskr` directory and add the `__init__.py` file. The `__init__.py` server double duty: it will contain the application factory, and it tells Python that the `flaskr` directory should be treated as a package.

> [flask/__init\__.py](https://github.com/romuro-pauliv/Introduction-to-Flask/blob/main/flask-tutorial/flaskr/__init__.py)

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
    + `instance_relative_config=True` tells the app that configuration files are relative to the instance folder. The instance folder is located outside the `flaskr` package and can hold local data that shouldn't be committed to version control, such as configuration secrets and the database file.

2. **app.config.from_mapping( )** sets some default configuration that the app will use:
    + **SECRET_KEY** is used by Flask and extensions to keep data safe. It's set to `'dev'` to provide a convenient value during development, but it should be overridden with a random value when deploying.
    + `DATABASE` is the path where the SQLite database file will be saved. It's under **app.instance_path**, which is the path that Flask has chosen for the instance folder. You'll learn more about the database in the next section.

3.  **app.config.from_pyfile( )** overrides the default configuration values taken from the config.py file in the instance folder if it exists. For example, when deploying, this can be used to set a real `SECRET_KEY`.
    + `test_config` can also be passed to the factory, and will be used instead of the instance configuration. This is so the tests you'll write later in the tutorial can be configured independently of any development values you have configured. 

4. **os.makedirs( )** ensures that app.instance_path exists. Flask doesn't create the instance folder automatically, but it needs to be created because your project will create the SQLite database file there.

5. **@app.route( )** creates a simple route so you can see the application working before getting into the rest of the tutorial. It creates a connection between the URL `/hello` and a function that returns a response, the string `'Hello, World!'` in this case.

----
#### Run the application

Now you can run your application using the flask command. From the terminal, tell Flask where to find your application, then run it in debug mode. Remember, you should still be in the top-level `flask-tutorial` directory, not the `flaskr` package.

Debug mode shows an interactive debugger whenever a page raises an exception, and restarts the server whenever you make changes to the code. You can leave it running and just reload the browser page as you follow the tutorial.

`flask --app flaskr --debug run`

You'll see output similar to this:

```
* Serving Flask app "flaskr"
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: nnn-nnn-nnn
```

Visit http://127.0.0.1:5000/hello in a browser an you should see the "Hello, World!" message. Congratulations, you're now running your Flask web application!

If another program is already using port 5000, you'll see `OSError: [Errno 98]` or `OSError: [WinError 10013]` when the server tries to start.

----

- We recommend that you view the code [__init\__.py](https://github.com/romuro-pauliv/Introduction-to-Flask/blob/main/flask-tutorial/flaskr/__init__.py)
- Continue to [Define and Access the Database](https://github.com/romuro-pauliv/Introduction-to-Flask/blob/main/flask-tutorial/flaskr/md/database.md)

----