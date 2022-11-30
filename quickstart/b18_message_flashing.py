# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                  quickstart.18_message_flashing.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# +------------------+
# | Message Flashing |
# +------------------+

"""
Good applications and user interfaces are all about feedback. If the user does not get enough feedback they will proba -
bly end up hating the application. Flask provides a really simple way to give feedback to a user with the flashing sys -
tem. The flashing system basically makes it possible to record a message at the end of a request and access it on the 
nex (and oly the next) request. This is usually combined with a layout template to expose the message.

To flask a message use the flash() method, to get hold of the messages you can use get_flashed_messages() which is also
avaiable in the templates. See above for a full example:
https://flask.palletsprojects.com/en/2.2.x/patterns/flashing/
"""

