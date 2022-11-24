# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                       quickstart.13_file_upload.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# +-------------+
# | File Upload |
# +-------------+

"""
You can handle uploaded files with Flask easily. Just make sure not to forget to set the enctype="multipart/form-data"
attribute on your HTML form. otherwise the browser will not transmit your files at all.

Uploaded files are stored in memory or at a temporary location on the filesystem. You can access those files by looking
at the files attribute on the request object. Each uploaded file is stored in that dictionary. It behaves just like a 
standard Python file object, but it also has a save() method that allows you to store that file on the filesystem of the
server. Here is a simple example showing how that works:
"""

# +--------------------------------------------------------------------------------------------------------------------+
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
# +--------------------------------------------------------------------------------------------------------------------+


app = Flask(__name__)


@app.route('/upload')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'

"""
If you want to know how the file was named on the client before it was uploaded to your application, you can access the
filename attribute. However please keep in mind that this value can be forged so never ever trust that value. if you
want to use the filename of the client to store the file on the server, pass it through the secure_filename() function 
that Werkzeug provides for you
"""
