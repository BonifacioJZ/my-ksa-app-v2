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
from ..views.product import ProductListCreateView,ProductDetailView,ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product-list'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('<slug:slug>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('<slug:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]
