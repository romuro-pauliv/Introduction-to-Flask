# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                               quickstart.10_rendering_templates.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# +---------------------+
# | Rendering Templates |
# +---------------------+


"""
Generating HTML from within Python is not fun, and actually pretty cumbersome because you have to do the HTML escaping
on your own to keep application secure. Because of that Flask configures the JINJA2 template engine for you 
automatically

Templates can be used to generate any type of text file. For web applications, you'll primarily be generating HTMLpages,
but you can also generate markdown, plain text for emails, any anything else.

For a reference to HTML, CSS, and other web APIs, use the ![[[[MDN Web Docs]]]]!

To render a template you can use the render_template() method. All you have to do is provide the name of the template 
and variables you want to pass to the template engine as keyword arguments. Here's a simple example of how to render a 
template.
"""

# +--------------------------------------------------------------------------------------------------------------------+
from flask import Flask
from flask import render_template
# +--------------------------------------------------------------------------------------------------------------------+

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

"""
Flask will look for templates in the templates folder. So if your application is a module, this folder is next to that
module, if it's a package it's actually inside your package.
"""

# Case 1: a module:
"""
/application.py
/templates
    /hello.html
"""

# Case 2: a package:
"""
/application
    /__init__py
    /templates
        /hello.html
"""

"""
For templates you can use the full power of JINJA2 templates. Head over to the official Jinja2 Template Documentation:
https://jinja.palletsprojects.com/en/3.1.x/templates/
"""

# +------------------------------------------+
# | Template example in templates/hello.html |
# +------------------------------------------+

"""
Inside templates you also have access to the config, request, session and g objects as well as the url_for() and 
get_flashed_messages() functions.

Templates are especially useful if inheritance is used. if you want to know how that works, see Template Inheritance:
https://flask.palletsprojects.com/en/2.2.x/patterns/templateinheritance/

Basically template inheritance makes it possible to keep certain elements in each page
(like header, natigation and footer)

Automatic escaping is enabled, so if name contais HTML it will be escaped automatically. If you can trust a variable and
you know that it will be safe by using the Markup class or by using the |safe filter in the template. Head over to the
JINJA2 documentation for more examples.

Here is a basic introduction to how the Markup class works.
"""

"""
>>> from markupsafe import Markup
>>> Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
Markup('<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')

>>> Markup.escape('<blink>hacker</blink>')
Markup('&lt;blink&gt;hacker&lt;/blink&gt;')

>>> Markup('<em>Marked up</em> &raquo; HTML').striptags()
'Marked up » HTML' 
"""