from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^$', views.Carmodelrecommend_3knnb.as_view()),
	#url(r'^hello', views.Hello.as_view(), name="hello"),
]
