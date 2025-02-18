from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Rahul'

ifte('/')
de== "__main__":
    app.run(host='0.0.0.0', port=8080)
