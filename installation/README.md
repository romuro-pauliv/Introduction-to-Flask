# Installation

----
## Python Version

We recommend using the latest version of Python. Flask supports Python 3.7 and newer.

----
## Dependencies

These distributions will be installed automatically when installing Flask.

+ [Werkzeug](https://werkzeug.palletsprojects.com/en/2.2.x/) implements WSGI, the standard Python interface between applications and servers.
+ [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) is a template language that renders the pages your application serves.
+ [MarkupSage](https://markupsafe.palletsprojects.com/en/2.1.x/) comes with Jinja. It escapes untrusted input when rendering templates to avoid injection attacks.
+ [ItsDangerous](https://itsdangerous.palletsprojects.com/en/2.1.x/) securely signs data to ensure its integrity. This is used to protect Flask’s session cookie.
+ [Click](https://click.palletsprojects.com/en/8.1.x/) is a framework for writing command line applications. It provides the flask command and allows adding custom management commands.

----
### Optional dependencies

These distributions will not be installed automatically. Flask will detect and use them if you install them.

+ [Blinker](https://blinker.readthedocs.io/en/stable/) provides support for [Signal](https://flask.palletsprojects.com/en/2.2.x/signals/)
+ [python-dotenv](https://pypi.org/project/python-dotenv/) enables support for [Environment Variables From dotenv](https://flask.palletsprojects.com/en/2.2.x/cli/#dotenv) when running flask commands.
+ [Watchdog](https://pythonhosted.org/watchdog/) provides a faster, more efficient reloader for the development server.

----
### greenlet

You may choose to use gevent or eventlet with your application. In this case, greenlet>=1.0 is required. When using PyPy, PyPy>=7.3.7 is required.

These are not minimum supported versions, they only indicate the first versions that added necessary features. You should use the latest versions of each.

----

## Virtual environments

Use a virtual environment to manage the dependencies for your project, both in development and in production.

What problem does a virtual environment solve? The more Python projects you have, the more likely it is that you need to work with different versions of Python libraries, or even Python itself. Newer versions of libraries for one project can break compatibility in another project.

Virtual environments are independent groups of Python libraries, one for each project. Packages installed for one project will not affect other projects or the operating system’s packages.

Python comes bundled with the `venv` module to create virtual environments.

### Create an environment
In your project folder:
| OS | command line |
|----|--------------|
| Linux/macOS | `python3 -m venv venv`|
| Windows | `py -3 -m venv venv`|

### Activate the environment
Before you work on your project, activate the corresponding environment:
| OS | command line |
|----|--------------|
| Linux/macOS | `source venv/bin/activate`|
| Windows | `venv\Scripts\activate`|

Your shell prompt will change to show the name of the activated environment.

----
## Install Flask and dependencies
Within the activated environment, use the following command to install Flask:

`$ pip install flask`

I will also leave a file with all the project dependencies in case you prefer to do it all at once:

`pip install -r requirements.txt`

The tutorial will assume you're working from the fask-tutorial directory from now on. The file names at the top of each code block are relative to the directory.

----

Flask is now installed. Check out the [Quickstart](https://github.com/romuro-pauliv/Introduction-to-Flask/tree/main/quickstart) or go to the [Documentation Overview](https://github.com/romuro-pauliv/Introduction-to-Flask).

----