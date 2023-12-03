from django.urls import path,include
from . import views
from rest_framework import routers

app_name = 'characters'

router = routers.DefaultRouter()
router.register('characters', views.CharacterViewSet, basename='characters')

urlpatterns = [
    path('', include(router.urls)),
]