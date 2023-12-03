from django.urls import path,include
from . import views
from rest_framework import routers

app_name = 'items'

router = routers.DefaultRouter()
router.register('items', views.ItemViewSet, basename='items')

urlpatterns = [
    path('', include(router.urls)),
]