from django.urls import path,include
from . import views
from rest_framework import routers

app_name = 'effects'

router = routers.DefaultRouter()
router.register('effects', views.EffectViewSet, basename='effects')

urlpatterns = [
    path('', include(router.urls)),
]