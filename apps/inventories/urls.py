from django.urls import path,include
from . import views
from rest_framework import routers

app_name = 'inventories'

router = routers.DefaultRouter()
router.register('inventories', views.InventoryViewSet, basename='inventories'),
router.register('inventories_slots', views.InventorySlotsViewSet, basename='inventories_slots')

urlpatterns = [
    path('', include(router.urls)),
]