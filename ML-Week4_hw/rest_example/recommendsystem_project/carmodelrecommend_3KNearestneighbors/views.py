from django.shortcuts import render

# Create your views here.
import os
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import pickle
import numpy as np
import pandas as pd

class Carmodelrecommend_3knnb(APIView):

	def __init__(self):
		self.res_path = os.path.join(settings.PROJECT_ROOT, '..','carmodelrecommend_3KNearestneighbors', 'res')
		self.cardata_path = os.path.join(self.res_path, 'mtcars.csv')
		self.features_sample = [15, 300, 160, 3.2]
		self.cars = pd.read_csv(self.cardata_path)
		self.featues_len = len(self.features_sample)
		self.modelpath = os.path.join(self.res_path, 'carsNearestNeighborsX3.pickle')
		#print(self.modelpath)
		#print(self.cars)

	def get(self, request, *args, **kw):
		# Any URL parameters get passed in **kw
		result = {"mpg": 15, "disp": 300, "hp": 160, "wt": 3.2}
		response = Response(result, status=status.HTTP_200_OK)
		return response

	def post(self, request, *args, **kw):
		data = request.data
		# print(f"""	
		# 		Miles/(US) gallon: {data['mpg']} 
		# 		Displacement (cu.in.): {data['disp']}
		# 		Gross horsepower: {data['hp']}
		# 		Weight (1000 lbs): {data['wt']}
		# 		""")

		#features_in = self.features_sample
		features_in = list(data.values())
		#print(features_in)
		if len(features_in) != self.featues_len:
			result = {"error": "input length"}
			return Response(result, status=status.HTTP_400_BAD_REQUEST)

		pred = self.k3nnbrecommender(features_in)
		#print(type(pred))

		result = {"result": pred}
		response = Response(result, status=status.HTTP_200_OK)
		return response  		

	def k3nnbrecommender(self, features_in):
		# setup column name
		self.cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

		with open(self.modelpath,'rb') as f:
			loadCarsNearestNeighborsX3 = pickle.load(f)

		# predict
		pred = loadCarsNearestNeighborsX3.kneighbors([features_in])
		#print(pred)
		#print(pred[1])

		# return
		cars_recommend = []
		for idx in pred[1][0]:
			#dat_list = self.cars.iloc[idx].values.tolist()
			#dat_json = self.cars.iloc[idx].to_json()
			dat_dict = self.cars.iloc[idx].to_dict()
			#print(type(dat_dict))
			#print(dat_dict)
			cars_recommend.append(dat_dict)

		#print(cars_recommend)
		return cars_recommend
