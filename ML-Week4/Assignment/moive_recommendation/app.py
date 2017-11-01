from flask import Flask
from flask import jsonify
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

@app.route("/movie/<name>")
def hello(name):
    filename = "model/my_movie_model.pk"
    with open(filename, 'rb') as handle:
        my_movie_model = dict(pickle.load(handle))

    movie_name   = my_movie_model['movie_name']
    movie_list   = list(movie_name)
    corr_mat     = my_movie_model['corr_mat']

    try:
        movie_index  = movie_list.index(name)
        corr_movie   = corr_mat[movie_index]
        return jsonify({ "result" : list(movie_name[(corr_movie >= 0.9) & (corr_movie <= 1.0)])})
    except Exception as e:
        return jsonify({ "result" : []})
