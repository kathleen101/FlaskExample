import os
import base64
from urllib import request

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/add', methods=['GET', 'POST'])
def add():
    # if request.method == 'POST':
    #     number = int(request.form['number'])

    return render_template('add.jinja2')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 50000))
    app.run(host='0.0.0.0', port=port)

