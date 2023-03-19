from django.contrib import admin
from django.urls import path
from .views import usuarios_View,create_user_view, update_user_view, delete_user_view
from django.contrib.auth.decorators import login_required
from . import views


app_name = "usuarios"
urlpatterns = [
    path('usuarios/',login_required(usuarios_View.as_view(),login_url="/"),name="usurios_view"),
    path('nuevo-usuario/',login_required(create_user_view.as_view(),login_url="/"),name="create_new_user"),
    path('update-usuario/<int:pk>/',login_required(update_user_view.as_view(),login_url="/"),name="update_user"),
    path('delete-usuario/<int:pk>/',login_required(delete_user_view.as_view(),login_url="/"),name="delete_user")
]