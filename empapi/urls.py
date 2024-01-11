from django.urls import path
from empapi import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("employees",views.Empview,basename="employees"),

urlpatterns=[



    
]+router.urls
