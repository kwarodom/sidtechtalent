from django.db import models

# Create your models here.

import numpy as np
import pandas as pd
import sklearn
from sklearn.decomposition import TruncatedSVD

import os 
# get current path
dir_path = os.path.dirname(os.path.realpath(__file__))

class MoviesSuggester():
    @staticmethod
    def suggest(base_movie_name):
        columns = ['user_id', 'item_id', 'rating', 'timestamp']
        frame = pd.read_csv(dir_path + '/data/ml-100k/u.data', sep='\t', names=columns)
        columns = ['item_id', 'movie title', 'release date', 'video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
          'Animation', 'Childrens', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror',
          'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

        movies = pd.read_csv(dir_path + '/data/ml-100k/u.item', sep='|', names=columns, encoding='latin-1')
        movie_names = movies[['item_id', 'movie title']]
        combined_movies_data = pd.merge(frame, movie_names, on='item_id')
        
        rating_crosstab = pd.pivot_table(
            data=combined_movies_data, 
            values='rating', 
            index='user_id', 
            columns='movie title',
            fill_value=0
        )
        X = rating_crosstab.T

        SVD = TruncatedSVD(n_components=12, random_state=17)
        result_matrix = SVD.fit_transform(X)
        corr_mat = np.corrcoef(result_matrix)

        movies_name = rating_crosstab.columns
        movie_list = list(movies_name)

        base_movie_id = movie_list.index(base_movie_name)
        corr_mat_movies = corr_mat[base_movie_id]

        return list(movies_name[(corr_mat_movies <= 1.0) & (corr_mat_movies >= 0.9)])

    @staticmethod
    def popular():
        columns = ['user_id', 'item_id', 'rating', 'timestamp']
        frame = pd.read_csv(dir_path + '/data/ml-100k/u.data', sep='\t', names=columns)
        columns = ['item_id', 'movie title', 'release date', 'video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
          'Animation', 'Childrens', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror',
          'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

        movies = pd.read_csv(dir_path + '/data/ml-100k/u.item', sep='|', names=columns, encoding='latin-1')
        movie_names = movies[['item_id', 'movie title']]

        popular =  pd.DataFrame(frame.groupby('item_id')['rating'].count()).sort_values('rating', ascending=False)
        popular_movies = pd.merge(popular, movie_names, left_index=True, right_on='item_id')
        return popular_movies.head(5).set_index('movie title')['rating'].to_dict()
