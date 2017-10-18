from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import json
import math
from django.http import HttpResponse, HttpResponseRedirect
import os

#import data science libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
import json

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

class LinearRegressPredict(APIView):

    def get(self, request, *args, **kw):
        print("calling get method")
        # Any URL parameters get passed in **kw
        result = {"result": "model trained"}
        # model training ----------------------------------------------
        filename = './finalized_model.sav'
        print("import data")
        USAhousing = pd.read_csv('USA_Housing.csv')
        X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
                        'Avg. Area Number of Bedrooms', 'Area Population']]
        y = USAhousing['Price']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)
        print("Start Training Process...")
        lm = LinearRegression()
        lm.fit(X_train, y_train)
        pickle.dump(lm, open(filename, 'wb'))
        response = Response(result, status=status.HTTP_200_OK)
        return response

    def post(self, request, *args, **kw):
        msg_body = json.loads(request.body)
        # TODO check data validity before publish mqtt message to Azure
        print("msg_body: {}".format(msg_body))
        print(type(msg_body))
        X_test = pd.DataFrame.from_dict(msg_body, orient='index')
        print(X_test.T)
        filename = './finalized_model.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        pred = loaded_model.predict(X_test.T)
        print(pred)
        result = {"result": pred}
        response = Response(result, status=status.HTTP_200_OK)
        return response

class RecommenderSystem(APIView):

    def get(self, request, *args, **kw):
        print("calling get method")
        # Any URL parameters get passed in **kw
        result = {"result": "model trained"}
        # model training ----------------------------------------------
        filename = './finalized_model.sav'
        print("import data: mtcars")
        cars = pd.read_csv('mtcars.csv')
        cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
        X = cars.ix[:, (1, 3, 4, 6)].values
        nbrs = NearestNeighbors(n_neighbors=2).fit(X)
        print("Start Training Process...")
        pickle.dump(nbrs, open(filename, 'wb'))
        response = Response(result, status=status.HTTP_200_OK)
        return response

    def post(self, request, *args, **kw):
        msg_body = json.loads(request.body)
        # TODO check data validity before publish mqtt message to Azure
        print("msg_body: {}".format(msg_body))
        print(type(msg_body))
        X_test = pd.DataFrame.from_dict(msg_body, orient='index')

        # Verify features
        ind = X_test.index.values.tolist()

        if ind == ['mpg','disp','hp','wt']:

            X_temp = X_test.iloc[:, 0].tolist()
            print(X_temp)
            filename = './finalized_model.sav'
            loaded_model = pickle.load(open(filename, 'rb'))
            pred = loaded_model.kneighbors([X_temp])
            print(pred)

            # Result
            cars = pd.read_csv('mtcars.csv')
            cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
            car1 = cars.loc[pred[1][0][0], :]
            car2 = cars.loc[pred[1][0][1], :]
            print(car1)
            print(car2)
            result = {"result": [car1,car2]}
        else:
            print("Input format has to be [\"mpg\":10,\"disp\":10,\"hp\":10,\"wt\":10]")
            result = {"result": "Invalid Input"}

        response = Response(result, status=status.HTTP_200_OK)
        return response

