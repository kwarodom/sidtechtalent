from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# import ML model
from .recommender import MovieRecommender

MR = MovieRecommender()

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


class SuggestMovie(APIView):

    def get(self, request, format=None):
        return Response('This url only allow POST method')

    def post(self, request, format=None):
        movie_title = request.data['movie_title']
        result = MR.recommend(movie_title)
        return Response(result)
