from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from nearestNeighbors_api.serializers import UserSerializer, GroupSerializer

from django.utils.encoding import force_text
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.parsers import JSONParser

import json
import math

### API
#from api_nnp import nnp_cal
import numpy as np
import pandas as pd
import sklearn
from sklearn.neighbors import NearestNeighbors

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
   
class Hello(APIView):
    def get(self, request, *args, **kw):
        print("calling get method of Hello")
        # Any URL parameters get passed in **kw
        result = {"hello": "1234567"}
        response = Response(result, status=status.HTTP_200_OK)

        #return Response({"hello": "world"}) 
        return response

    def post(self, request, *args, **kw):
        print("calling post method of Hello")
        data = request.data
        pred = data
        result = {"result": pred}
        response = Response(result, status=status.HTTP_200_OK)
        return response  		

class World(APIView):
    def get(self, request, *args, **kw):
    	###########################
        temp_val = '+40C'
        html_ = f'''
                <!DOCTYPE html>
                <html lang=en>
                 <head>
                 </head>
                 <body>
                  <h1>My World!</h1>
                  <p>Temp: {temp_val} is very hot</p>
                </body>
                </html>''' 
        ##########################
        # html_ = """
        #         <!DOCTYPE html>
        #         <html lang=en>
        #          <head>
        #          </head>
        #          <body>
        #           <h1>My World!</h1>
        #           <p>Temp: {temp_val} is very hot</p>
        #         </body>
        #         </html>"""         
        return HttpResponse(html_)


class Nnb(APIView):
	def get(self, request, *args, **kw):    	
	    #response =  Response({"nnp": "val"}) 
	    
	    response =  Response(self.nnp_cal('input1')) 
	    return response    	

	def post(self, request, *args, **kw):
		print("calling post method of Nnb")
		# data = JSONParser().parse(request)
		# pred = data
		# result = {"result": pred}
		# response = Response(result, status=status.HTTP_200_OK)
		# return response  

		json_data = json.loads(request.POST)
		try:
			data =json_data['data']
		except KeyError:
			result = {}
			response = Response(result, status=status.HTTP_400_BAD_REQUEST)

		json_data = json.loads(request.body)
		result = {"result": json_data}
		response = Response(result, status=status.HTTP_200_OK)	


	def nnp_cal(self, input):
		return (
				{ 	
					input : 'yyy'
					,'inputzz' : 'yyy1'
				}
				,{ 
					'foo' : 'bar'
				},

			)

    