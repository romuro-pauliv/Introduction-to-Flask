# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                       flaskr.db.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# +--------------------------------+
# | Define and Access the Database |
# +--------------------------------+

"""
The application will use a SQLite database to store users and posts. Python comes with built-in support for SQLite in
the sqlite3 module.

SQLite is convenient because it doesn't require setting up a separate database server and is built-in to Python. However
if concurrent requests try to write to the database at the same time, they will slow down as each write happens sequen -
tially. Small applications won't notice this. Once you become big, you may want to switch to a different database.

The tutorial doesn't go into detail about SQL. If you are not familiar with it, the SQLite docs describe the language:
https://sqlite.org/lang.html
"""

