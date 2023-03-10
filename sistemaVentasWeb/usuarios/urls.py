from django.contrib import admin
from django.urls import include, path
from .views import usuarios_View,create_user_view, update_user_view
from django.contrib.auth.decorators import login_required


app_name = "usuarios"
urlpatterns = [
    path('usuarios/',login_required(usuarios_View.as_view(),login_url="/"),name="usurios_view"),
    path('nuevo-usuario/',login_required(create_user_view.as_view(),login_url="/"),name="create_new_user"),
    path('<int:pk>/update-usuario/',login_required(update_user_view.as_view(),login_url="/"),name="update_user")
]