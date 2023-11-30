from django.urls import path,include
from . import views
from rest_framework import routers

app_name = 'magics'

router = routers.DefaultRouter()
router.register('magics', views.MagicViewSet, basename='magics')

urlpatterns = [
    path('', include(router.urls)),
]