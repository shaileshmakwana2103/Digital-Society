"""digitalsociety URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from societymemberapp import views

urlpatterns = [
    path('societymember-profile/', views.societymember_profile, name='societymember-profile'),
    path('societymember-change-password/',views.societymember_change_password,name="societymember-change-password"),
    path('view-notice-society/',views.view_notice_society,name="view-notice-society"),
    path('view-notice-society_details/<int:pk>',views.view_notice_society_details,name="view-notice-society-details"),
    path('view-events-society/',views.view_events_society,name="view-events-society"),
    path('view-events-society_details/<int:pk>',views.view_events_society_details,name="view-events-society-details"),
    path('add-complaints/',views.add_complaints,name="add-complaints"),
    path('view-complaints/',views.view_complaints,name="view-complaints"),
    path('view-complaints-details/<int:pk>',views.view_complaints_details,name="view-complaints-details"),

     
]
