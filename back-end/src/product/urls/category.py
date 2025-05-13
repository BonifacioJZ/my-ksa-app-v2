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
from ..views.category import CategoryListCreateView,CategoryRetrieveView,CategoryUpdateView,CategoryDeleteView
urlpatterns = [
    path('',CategoryListCreateView.as_view(), name='category-list-create'),
    path('<slug:slug>/', CategoryRetrieveView.as_view(), name='category-detail'),
    path('<slug:slug>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('<slug:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
]
