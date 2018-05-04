import numpy as np
import pandas as pd
from flask import Flask
from flask import request
from flask import render_template
from DBSCAN import *
import json


app = Flask(__name__)

@app.route("/")
def hello():
    # word = request.args.get('anuraag','default')
    # word2 = request.get_json()
    # return word
    return render_template('index.html')

@app.route("/jq.js")
def jq():
    # word = request.args.get('anuraag','default')
    # word2 = request.get_json()
    # return word
    return render_template('jq.js')

@app.route("/cluster", methods=['GET'])
def cluster():
    coordinates = request.args.get('coordinates')
    epsilon = float(request.args.get('epsilon'))
    min_pts = float(request.args.get('min_pts'))
    print(epsilon,min_pts)
    dbs = DBSCAN(epsilon,min_pts)
    print('Working')
    d = json.loads(coordinates)
    data = np.array([ float(d[0]['x']),float(d[0]['y']) ])
    for i in np.arange(1,len(d)):
        data = np.vstack((data, [ float(d[i]['x']), float(d[i]['y']) ] ))
    label = dbs.cluster(data)
    # ret = json.dumps({'labels' : label})
    ret = pd.Series(label).to_json(orient='values')
    return ret


if __name__ == "__main__":
    app.run()
