from django.urls import path,include
from . import views
from rest_framework import routers

app_name = 'itemcategories'



router = routers.DefaultRouter()
router.register('itemcategories', views.ItemCategoryViewSet, basename='itemcategories')

urlpatterns = [
    path('', include(router.urls)),
]