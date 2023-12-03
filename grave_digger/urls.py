"""
URL configuration for grave_digger project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rarities', include('rarities.urls', namespace='rarities')),
    path('effects', include('effects.urls', namespace='effects')),
    path('itemcategories', include('itemcategories.urls', namespace='itemcategories')),
    path('magics', include('magics.urls', namespace='magics')),
    path('items', include('items.urls', namespace='items')),
    path('characters', include('characters.urls', namespace='characters')),
    path('inventories', include('inventories.urls', namespace='inventories'))
]
