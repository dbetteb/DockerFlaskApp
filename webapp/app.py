# app.py simple api written in Flask 

from flask import Flask

app = Flask(__name__)

@app.route('/users/<string:username>')
def hello_ekimetrics(username=None):
    return "Welcome {} to Ekimetrics !".format(username)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8000)

