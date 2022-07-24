import os
from flask import Flask
app = Flask(__name__)


@app.route('/hello/')
def hello_world():
    return 'Hello, World'


@app.route('/hello/<name>/')
def hello_name(name):
    return 'Hello, {}'.format(name)


@app.route('/goodbye/<times>/<name>/')
def goodbye(name, times):
    try:
        return(f'Goodbye {name}!')*int(times)
    except:
        return f'Goodbye{name}!'


# http://127.0.0.1:50000/hello/
# http://127.0.0.1:50000/hello/kathleen/
# http://127.0.0.1:50000/goodbye/3/kathleen/



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 50000))
    app.run(host='0.0.0.0', port=port, debug=True)
