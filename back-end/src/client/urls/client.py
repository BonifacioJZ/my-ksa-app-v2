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

from django.urls import path
from ..views.client import ClientListCreateView,ClientRetrieveView, ClientUpdateView, ClientDeleteView
urlpatterns = [
    path('', ClientListCreateView.as_view(), name='client-list-create'),
    path('<slug:slug>/', ClientRetrieveView.as_view(), name='client-detail'),
    path('<slug:slug>/update/', ClientUpdateView.as_view(), name='client-update'),
    path('<str:pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),
]
