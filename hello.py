from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    # word = request.args.get('anuraag','default')
    # word2 = request.get_json()
    # return word
    return render_template('index.html')

@app.route("/cluster", methods=['GET'])
def cluster():
    coordinates = request.args.get('coordinates')
    dbs = DBSCAN()
    return coordinates


if __name__ == "__main__":
    app.run()
