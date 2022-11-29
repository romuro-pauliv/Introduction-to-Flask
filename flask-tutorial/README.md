### Tutorial

This tutorial will walk you through creating a basic blog application called Flaskr. User wll be able to register, log in, create posts, and edit or delete their own posts. You will be able to package and install the application on other computers.

It's assumed that you're already familiar with Python. The official tutorial in the Python docs is a great way to learn or review first.

While it's desined to give a good starting point, the tutorial doesn't cover all of Flask's features. Check out the quickstart for an overview of what Flask can do, then dive into the docs to find out more. The tutorial only user what's provided by Flask and Python. In another project, you might decide to use Extensions or other libraries to make some task simpler.

Flask is flexibe. It doesn't require you to use any particular project or code layout. However, when first starting, it's helpful to use a more structure approach. This means that the tutorial will require a bit of boilerplate up front, but it's done to avoid many common pitfalls that new developer encounter, and it creates a project that's easy to expand on. Once you become more confortable with Flask, you can step out of this structure and take full advantage of Flask's flexibility.

----

#### Project Layout

Use a virtual environment to manage the dependencies for your project, both in development and in production.

What problem does a virtual environment solve? The more Python projects you have, the more likely it is that you need to work with different versions of Python libraries, or even projects itself. Newer versions of libraries of one project can break compatibility in another project.

Virtual environment are independent groups of Python libraries, one for each project. Packages installed for one project will not affect other projects or the operating system's packages.

Python comes bundled with the venv module to create a virtual environments.

##### Create an environment
In your project folder:
| OS | command line |
|----|--------------|
| Linux/macOS | `python3 -m venv venv`|
| Windows | `py -3 -m venv venv`|

##### Activate the environment
Before you work on your project, activate the corresponding environment:
| OS | command line |
|----|--------------|
| Linux/macOS | `source venv/bin/activate`|
| Windows | `venv\Scripts\activate`|

Your shell prompt will change to show the name of the activated environment.

----
##### Install Flask and dependencies
Within the activated environment, use the following command to install Flask:

`$ pip install flask`

I will also leave a file with all the project dependencies in case you prefer to do it all at once:

`pip install -r requirements.txt`

The tutorial will assume you're working from the fask-tutorial directory from now on. The file names at the top of each code block are relative to the directory.

A Flask application can be as simple as single file. See [minimal_application.py](link). However, as project gets bigger, it becomes overwhelming to keep all the code in one file. Python projects use packages to organize code into multiple modules that can be imported where needed, and the tutorial will do this as well.

----

##### Layout

The project directory will contain:
- `flaskr/`, a Python package containing your application code and files.
- `tests/`, a directory containing test modules.
- `venv/`, a Python virtual environment where Flask and other dependencies are installed.
- Installation files teling Python how to install your project.
- Version control config, such as git. You should make a habit of using some type of version control for all your projects, no matter the size.
- Any other project file you might add in the future.

By the end, your project layout will look like this:

```
/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in
```

If you're using version control, the following files that are generated while running your project should be ignored. There may be files based on the editor you use. In general, ignore files that you didn't write. For example, with git:

**.gitignore**
```
venv/

*.pyc
__pycache__/

instance/

.pytest_cache/
.coverage
htmlcov/

dist/
build/
*.egg-info/
```
----

### Application Setup

A Flask application is an instance of the **Flask** class. Everything about the application, such as configuration and URLs, will be registered with the class.

The most straightforward way to create a Flask application is to create a global **Flask** instance directly at the top of your code, like how the "Hello, World" example in [quickstart](). While this is sample and useful in some cases, it can cause some tricky issues as the project grows.

Instead of creating a **Flask** instance globally, you will create it inside a function. This function is known as the _aplication factory_. Any configuration, registration, and other setup the application needs will hapen inside the function, then the application will be returned.

----

#### The Application Factory

It's time to start coding! Create the `flaskr` directory and add the `__init__.py`file. The `__init__.py` server double duty: it will contain the application factory, and it tells Python that the `flaskr` directory should be treated as a package.

`$ mkdir flaskr`

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
