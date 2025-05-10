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
from ..views.presentation import PresentationCreateListView,PresentationRetrieveView,PresentationUpdateView,PresentationDeleteView
urlpatterns = [
    path('', PresentationCreateListView.as_view(), name='presentation-list-create'),
    path('<slug:slug>/', PresentationRetrieveView.as_view(), name='presentation-detail'),
    path('<slug:slug>/update/', PresentationUpdateView.as_view(), name='presentation-update'),
    path('<slug:pk>/delete/', PresentationDeleteView.as_view(), name='presentation-delete'),
    
]
