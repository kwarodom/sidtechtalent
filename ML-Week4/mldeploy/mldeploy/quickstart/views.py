#from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from mldeploy.quickstart.serializers import UserSerializer, GroupSerializer




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.externals import joblib


from sklearn.decomposition import TruncatedSVD

class Wines(APIView):
    def get(self, request, format=None):
        # 3. Load red wine data.
        dataset_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
        data = pd.read_csv(dataset_url, sep=';')

        # 4. Split data into training and test sets
        y = data.quality
        X = data.drop('quality', axis=1)
        X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                            test_size=0.2,
                                                            random_state=123,
                                                            stratify=y)

        # 5. Declare data preprocessing steps
        pipeline = make_pipeline(preprocessing.StandardScaler(),
                                 RandomForestRegressor(n_estimators=100))

        # 6. Declare hyperparameters to tune
        hyperparameters = {'randomforestregressor__max_features': ['auto', 'sqrt', 'log2'],
                           'randomforestregressor__max_depth': [None, 5, 3, 1]}

        # 7. Tune model using cross-validation pipeline
        clf = GridSearchCV(pipeline, hyperparameters, cv=10)

        clf.fit(X_train, y_train)

        # 8. Refit on the entire training set
        # No additional code needed if clf.refit == True (default is True)

        # 9. Evaluate model pipeline on test data
        pred = clf.predict(X_test)
        # print r2_score(y_test, pred)
        # print mean_squared_error(y_test, pred)

        # 10. Save model for future use
        joblib.dump(clf, 'rf_regressor.pkl')
        # To load: clf2 = joblib.load('rf_regressor.pkl')
        return Response({'result': 'train model success'})
    def post(self, request, format=None):
        # 3. Load red wine data.
        dataset_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
        data = pd.read_csv(dataset_url, sep=';')

        # 4. Split data into training and test sets
        y = data.quality
        X = data.drop('quality', axis=1)
        X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                            test_size=0.2,
                                                            random_state=123,
                                                            stratify=y)
        clf2 = joblib.load('rf_regressor.pkl')

        # Predict data set using loaded model
        pred = clf2.predict(X_test)
        return Response({'result': pred})

class UserList(APIView):
    def get(self, request, format=None):
        # 3. Load red wine data.
        dataset_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
        data = pd.read_csv(dataset_url, sep=';')

        # 4. Split data into training and test sets
        y = data.quality
        X = data.drop('quality', axis=1)
        X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                            test_size=0.2,
                                                            random_state=123,
                                                            stratify=y)

        # 5. Declare data preprocessing steps
        pipeline = make_pipeline(preprocessing.StandardScaler(),
                                 RandomForestRegressor(n_estimators=100))

        # 6. Declare hyperparameters to tune
        hyperparameters = {'randomforestregressor__max_features': ['auto', 'sqrt', 'log2'],
                           'randomforestregressor__max_depth': [None, 5, 3, 1]}

        # 7. Tune model using cross-validation pipeline
        clf = GridSearchCV(pipeline, hyperparameters, cv=10)

        clf.fit(X_train, y_train)

        # 8. Refit on the entire training set
        # No additional code needed if clf.refit == True (default is True)

        # 9. Evaluate model pipeline on test data
        pred = clf.predict(X_test)
        #print r2_score(y_test, pred)
        #print mean_squared_error(y_test, pred)

        # 10. Save model for future use
        joblib.dump(clf, 'rf_regressor.pkl')
        # To load: clf2 = joblib.load('rf_regressor.pkl')
        return Response({'result': 'train model success'})
    def post(self, request, format=None):
        return Response({'result': 'bb'})

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class Recommends(APIView):
    def get(self, request, format=None):
        columns = ['user_id', 'item_id', 'rating', 'timestamp']
        frame = pd.read_csv('ml-100k/u.data', sep='\t', names=columns)
        columns = ['item_id', 'movie title', 'release date', 'video release date', 'IMDb URL', 'unknown', 'Action',
                   'Adventure',
                   'Animation', 'Childrens', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir',
                   'Horror',
                   'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

        movies = pd.read_csv('ml-100k/u.item', sep='|', names=columns, encoding='latin-1')
        movie_names = movies[['item_id', 'movie title']]
        combined_movies_data = pd.merge(frame, movie_names, on='item_id')
        filter = combined_movies_data['item_id'] == 50
        combined_movies_data[filter]['movie title'].unique()
        rating_crosstab = pd.pivot_table(data=combined_movies_data, values='rating', index='user_id',
                                         columns='movie title', fill_value=0)
        #rating_crosstab.head()
        X = rating_crosstab.T
        #X.shape
        SVD = TruncatedSVD(n_components=12, random_state=17)
        resultant_matrix = SVD.fit_transform(X)
        corr_mat = np.corrcoef(resultant_matrix)
        joblib.dump(corr_mat, 'corr_mat.pkl')

        corr_mat_load = joblib.load('corr_mat.pkl')

        #movie_names = rating_crosstab.columns
        #movies_list = list(movie_names)
        #star_wars = movies_list.index('Star Wars (1977)')
        #corr_star_wars = corr_mat_load[star_wars]  #1398
        #result = list(movie_names[(corr_star_wars < 1.0) & (corr_star_wars > 0.95)])

        return Response({'result': 'Train Model Success'})
    def post(self, request, format=None):
        columns = ['user_id', 'item_id', 'rating', 'timestamp']
        frame = pd.read_csv('ml-100k/u.data', sep='\t', names=columns)
        columns = ['item_id', 'movie title', 'release date', 'video release date', 'IMDb URL', 'unknown', 'Action',
                   'Adventure',
                   'Animation', 'Childrens', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir',
                   'Horror',
                   'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

        movies = pd.read_csv('ml-100k/u.item', sep='|', names=columns, encoding='latin-1')
        movie_names = movies[['item_id', 'movie title']]
        combined_movies_data = pd.merge(frame, movie_names, on='item_id')
        filter = combined_movies_data['item_id'] == 50
        combined_movies_data[filter]['movie title'].unique()
        rating_crosstab = pd.pivot_table(data=combined_movies_data, values='rating', index='user_id',
                                         columns='movie title', fill_value=0)
        # rating_crosstab.head()
        #X = rating_crosstab.T
        # X.shape
        #SVD = TruncatedSVD(n_components=12, random_state=17)
        #resultant_matrix = SVD.fit_transform(X)
        #corr_mat = np.corrcoef(resultant_matrix)
        #joblib.dump(corr_mat, 'corr_mat.pkl')
        target_movie_name = request.data['movie_name']
        corr_mat_load = joblib.load('corr_mat.pkl')

        movie_names = rating_crosstab.columns
        movies_list = list(movie_names)
        star_wars = movies_list.index(target_movie_name[0])
        corr_star_wars = corr_mat_load[star_wars]  # 1398
        result = list(movie_names[(corr_star_wars < 1.0) & (corr_star_wars > 0.95)])

        return Response({'result': result})


