from django.contrib import admin
from django.urls import include, path
from .views import usuarios_View

app_name = "usuarios"
urlpatterns = [
    path('usuarios/',usuarios_View.as_view(),name="usurios_view"),
]