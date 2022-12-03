### Blog blueprint

You'll use the same techniques you learned about when writing the authentication blueprint to write the blog blueprint. The blog should list all posts, allow logged in users to create posts. and allow the author of a post to edit or delete it.

As you implement each view, keep the development server running. As you save your changes, try going to the URL in your browser and testing them out.

----

### The Blueprint

Define the blueprint and register it in the application factory.

> [flaskr/blog.py]()
```Python
from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db
```

Import and register the blueprint from the factory using **app.register.blueprint()**. Place the new code at ht end of the end of the factory function before returning the app.

> [flaskr/__init\__.py]()

```Python
```
