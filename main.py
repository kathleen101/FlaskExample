import os
import base64
from urllib import request

from flask import Flask, request, render_template, session

from model import SavedTotal

app = Flask(__name__)
app.secret_key = b'&\x81\xed\t\sbd\scd\se2\s90B\x1a\xf0\xba\x8e*\xa7m9\x8az\xcehtD'


@app.route('/add', methods=['GET', 'POST'])
def add():
    if 'total' not in session:
        session['total'] = 0

    if request.method == 'POST':
        number = int(request.form['number'])
        session['total'] += number

    return render_template('add.jinja2', session=session)


@app.route('/save', methods=['POST'])
def save():
    total = session.get('total', 0)
    code = base64.b32encode(os.urandom(8)).decode().strip("=")

    saved_total = SavedTotal(value=total, code=code)
    saved_total.save()

    return render_template('save.jinja2', code=code)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 50000))
    app.run(host='0.0.0.0', port=port, debug=True)

