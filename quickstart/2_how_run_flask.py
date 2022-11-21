# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                        quickstart.how_run_flask.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# +--------------------------------+
# | Application Discovery Behavior |
# +--------------------------------+

"""
As a shortcut, if the file is named app.py or wsgi.py you dont't gave to use --app. See in below for more details:
https://flask.palletsprojects.com/en/2.2.x/cli/
"""

"""
This launches a very simple builtin server, which is good enough for testing but probably not what you want to use in
production. For deployment options see:
https://flask.palletsprojects.com/en/2.2.x/deploying/
"""

"""
Now head over to http://127.0.0.1:5000/, and you should see your hello world greeting. 
If another program is already using port 5000, you'll see OSError: [Errno 98] or OSError: [WinError 10013] when the
server tries to start. See the link below for how to handle that:
https://flask.palletsprojects.com/en/2.2.x/deploying/
"""

# +---------------------------+
# | Externally Visible Server |
# +---------------------------+

"""
If you run the server you will notice that the server is only accessible from your own computer, not from any other in
the network. this is the default because in debugging mode a user of the application can execute arbitraty Python code
on your computer.

If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply
by adding --host=0.0.0.0 to the command line:

$ flask run --host=0.0.0.0

This tells your operating system to listen on all public IPs.
"""

# +------------+
# | Debug mode |
# +------------+

