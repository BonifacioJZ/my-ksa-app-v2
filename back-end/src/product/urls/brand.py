"""
URL configuration for core project.

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

from django.urls import path, include
from ..views.brand import BrandListCreateView,BrandRetrieveApiView,BrandUpdateApiView,BrandDeleteApiView
urlpatterns = [
    path('', BrandListCreateView.as_view(), name='brand-list-create'),
    path('<slug:slug>/',BrandRetrieveApiView.as_view(), name='brand-detail'),
    path('<slug:slug>/update/', BrandUpdateApiView.as_view(), name='brand-update'),
    path('<slug:pk>/delete/', BrandDeleteApiView.as_view(), name='brand-delete'),

]
