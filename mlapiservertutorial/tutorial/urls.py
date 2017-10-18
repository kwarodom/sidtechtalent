from django.conf.urls import url, include
from rest_framework import routers
from sidmlapi import views as sidmlapiviews

router = routers.DefaultRouter()
router.register(r'users', sidmlapiviews.UserViewSet)
router.register(r'groups', sidmlapiviews.GroupViewSet)
# router.register(r'linearregress_predict', sidmlapiviews.LinearRegressPredict)
# router.register(r'predict', sidmlapiviews.Predict)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^api/v1.0/get_prediction[/]?$', sidmlapiviews.LinearRegressPredict.as_view(), name='my_rest_view'),
    url(r'^api/v1.0/get_prediction[/]?$', sidmlapiviews.RecommenderSystem.as_view(), name='my_rest_view'),
]