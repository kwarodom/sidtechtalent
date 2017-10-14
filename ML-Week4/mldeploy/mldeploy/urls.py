from django.conf.urls import url, include
from rest_framework import routers

from mldeploy.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^users/', views.UserList.as_view()),
    url(r'^wines/', views.Wines.as_view()),
    url(r'^recommends/', views.Recommends.as_view()),
    #url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
]