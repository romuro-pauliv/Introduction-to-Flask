### Application Setup

A Flask application is an instance of the **Flask** class. Everything about the application, such as configuration and URLs, will be registered with the class.

The most straightforward way to create a Flask application is to create a global **Flask** instance directly at the top of your code, like how the "Hello, World" example in [quickstart](https://github.com/romuro-pauliv/Introduction-to-Flask/tree/main/quickstart). While this is a sample and useful in some cases, it can cause some tricky issues as the project grows.

Instead of creating a **Flask** instance globally, you will create it inside a function. This function is known as the _application factory_. Any configuration, registration, and other setup the application needs will happen inside the function, then the application will be returned.

----

#### Reading Method

We recommend that you read the codes and documents in this order:

| Document | Info |
|----------|------|
| [flaskr/md/init.md](https://github.com/romuro-pauliv/Introduction-to-Flask/blob/main/flask-tutorial/flaskr/md/init.md) | The application factory |
| [flaskr/md/database.md](https://github.com/romuro-pauliv/Introduction-to-Flask/blob/main/flask-tutorial/flaskr/md/database.md) | Define and Access the Database |
| [flaskr/md/auth.md](https://github.com/romuro-pauliv/Introduction-to-Flask/blob/main/flask-tutorial/flaskr/md/auth.md) | Blueprint and views |
| [flaskr/md/template.md](https://github.com/romuro-pauliv/Introduction-to-Flask/blob/main/flask-tutorial/flaskr/md/template.md) | Templates |
| [flaskr/md/static.md](https://github.com/romuro-pauliv/Introduction-to-Flask/blob/main/flask-tutorial/flaskr/md/static.md) | Static files |
| [flaskr/md/blog.md](https://github.com/romuro-pauliv/Introduction-to-Flask/blob/main/flask-tutorial/flaskr/md/blog.md) | Blog |
| [flaskr/md/make_installable.md](https://github.com/romuro-pauliv/Introduction-to-Flask/blob/main/flask-tutorial/flaskr/md/make_installable.md) | Make the Project Installable |
| [tests/README.md](https://github.com/romuro-pauliv/Introduction-to-Flask/tree/main/flask-tutorial/tests) | Test Coverage |