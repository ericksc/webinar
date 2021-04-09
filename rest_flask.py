import flask
from flask import request, jsonify
import pandas as pd

app = flask.Flask(__name__)

dataset_df = pd.read_csv('netflix_titles.csv')

# endpoint
@app.route('/type/all')
def todos_los_generos_all():
    return jsonify(dataset_df.type.unique().tolist())

@app.route('/actors/all')
def todos_los_actores_all():
    return jsonify([pelicula.split(',') for pelicula in dataset_df.cast.unique().tolist() if pd.notna(pelicula)])


if __name__ == '__main__':
    app.run()
