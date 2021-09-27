from django.urls import include, path

from .views import ResultsViewset, ResultsPushViewset, ResultsShowViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', ResultsViewset, basename='/')
router.register('calculate/(?P<number1>\d+)/(?P<number2>\d+)', ResultsPushViewset, basename='calculate')
router.register('get_answer/(?P<identifier>\d+)', ResultsShowViewset, basename='answer')

urlpatterns = [
    path('', include(router.urls)),
]
