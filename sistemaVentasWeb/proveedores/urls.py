from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
from . import views

app_name = "proveedores"
urlpatterns = [
  path('proveedores/',login_required(providers_view.as_view(),login_url='/'),name='providers_view'),
  path('nuevo-proveedor/',login_required(create_providers_view.as_view(),login_url="/"),name="create_new_provider"),
]