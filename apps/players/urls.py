from django.urls import path,include
from . import views
from rest_framework import routers

app_name = 'players'

router = routers.DefaultRouter()
router.register('players', views.PlayerViewSet, basename='players'),

urlpatterns = [
    path('', include(router.urls)),
]