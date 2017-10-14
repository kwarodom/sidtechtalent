"""recommendsystem_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from nearestNeighbors_api import views as nnbapiviews

router = routers.DefaultRouter()
router.register(r'users', nnbapiviews.UserViewSet)
router.register(r'groups', nnbapiviews.GroupViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),    
    url(r'^nearestNeighbors_api/hello', nnbapiviews.Hello.as_view(), name="hello"),
    url(r'^nearestNeighbors_api/world', nnbapiviews.World.as_view(), name="world"),
	url(r'^nearestNeighbors_api/nnb', nnbapiviews.Nnb.as_view(), name="wnnb"),
    url(r'^admin/', admin.site.urls),
    url(r'^carrecommend_3nnb/', include('carmodelrecommend_3KNearestneighbors.urls')),
]
