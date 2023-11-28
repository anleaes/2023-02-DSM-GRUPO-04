from django.urls import path, include
from .import views
from rest_framework import routers


app_name = 'rarities'

router = routers.DefaultRouter()
router.register('rarities', views.RarityViewSet, basename='rarities')

urlpatterns = [
    path('', include(router.urls)),
]


