#### Summary
- [Tutorial](https://github.com/romuro-pauliv/Introduction-to-Flask/tree/main/flask-tutorial#tutorial)
- [Project layout](https://github.com/romuro-pauliv/Introduction-to-Flask/tree/main/flask-tutorial#project-layout)
    + [Create an environment](https://github.com/romuro-pauliv/Introduction-to-Flask/tree/main/flask-tutorial#create-an-environment)
    + [Install Flask and dependencies](https://github.com/romuro-pauliv/Introduction-to-Flask/tree/main/flask-tutorial#install-flask-and-dependencies)
    + [Directory layout](https://github.com/romuro-pauliv/Introduction-to-Flask/tree/main/flask-tutorial#layout)
- [Reading method](https://github.com/romuro-pauliv/Introduction-to-Flask/tree/main/flask-tutorial#reading-method)

----
### Tutorial

This tutorial will walk you through creating a basic blog application called Flaskr. The user wll be able to register, log in, create posts, and edit or delete their own posts. You will be able to package and install the application on other computers.

It's assumed that you're already familiar with Python. The official tutorial in the Python docs is a great way to learn or review first.

While it's designed to give a good starting point, the tutorial doesn't cover all of Flask's features. Check out the [Quickstart](https://github.com/romuro-pauliv/Introduction-to-Flask/tree/main/quickstart) for an overview of what Flask can do, then dive into the docs to find out more. The tutorial only used what's provided by Flask and Python. In another project, you might decide to use Extensions or other libraries to make some task simpler.

Flask is flexible. It doesn't require you to use any particular project or code layout. However, when first starting, it's helpful to use a more structured approach. This means that the tutorial will require a bit of boilerplate up front, but it's done to avoid many common pitfalls that new developer encounters, and it creates a project that's easy to expand on. Once you become more comfortable with Flask, you can step out of this structure and take full advantage of Flask's flexibility.

----

#### Project Layout

Use a virtual environment to manage the dependencies for your project, both in development and in production.

What problem does a virtual environment solve? The more Python projects you have, the more likely it is that you need to work with different versions of Python libraries, or even projects itself. Newer versions of libraries of one project can break compatibility in another project.

The virtual environment is independent groups of Python libraries, one for each project. Packages installed for one project will not affect other projects or the operating system's packages.

Python comes bundled with the venv module to create a virtual environments.

#### Create an environment
In your project folder:
| OS | command line |
|----|--------------|
| Linux/macOS | `python3 -m venv venv`|
| Windows | `py -3 -m venv venv`|

#### Activate the environment
Before you work on your project, activate the corresponding environment:
| OS | command line |
|----|--------------|
| Linux/macOS | `source venv/bin/activate`|
| Windows | `venv\Scripts\activate`|

Your shell prompt will change to show the name of the activated environment.

----
#### Install Flask and dependencies
Within the activated environment, use the following command to install Flask:

`$ pip install flask`

I will also leave a file with all the project dependencies in case you prefer to do it all at once:

`pip install -r requirements.txt`

The tutorial will assume you're working from the fask-tutorial directory from now on. The file names at the top of each code block are relative to the directory.

----

A Flask application can be as simple a single file. See [minimal_application.py](https://github.com/romuro-pauliv/Introduction-to-Flask/blob/main/quickstart/1_minimal_application.py). However, as the project gets bigger, it becomes overwhelming to keep all the code in one file. Python projects use packages to organize code into multiple modules that can be imported where needed, and the tutorial will do this as well.

#### Layout

The project directory will contain:
- `flaskr/`, a Python package containing your application code and files.
- `tests/`, a directory containing test modules.
- `venv/`, a Python virtual environment where Flask and other dependencies are installed.
- Installation files telling Python how to install your project.
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

> **.gitignore**
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

#### Reading Method

We recommend that you read the codes and documents in this order:

| Document | Info |
|----------|------|
| [flaskr/README.md](https://github.com/romuro-pauliv/Introduction-to-Flask/tree/main/flask-tutorial/flaskr) | Application Setup |
| [flaskr/md/init.md](https://github.com/romuro-pauliv/Introduction-to-Flask/blob/main/flask-tutorial/flaskr/md/init.md) | The application factory |
| [flaskr/md/database.md](https://github.com/romuro-pauliv/Introduction-to-Flask/blob/main/flask-tutorial/flaskr/md/database.md) | Define and Access the Database |
| [flaskr/md/auth.md](https://github.com/romuro-pauliv/Introduction-to-Flask/blob/main/flask-tutorial/flaskr/md/auth.md) | Blueprint and views |