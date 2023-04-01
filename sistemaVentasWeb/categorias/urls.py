from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
from . import views

app_name = "categorias"
urlpatterns = [
    path('categorias/',login_required(Categories_view.as_view(),login_url="/"),name="categories_view"),
    path('nueva-categoria/',login_required(create_category_view.as_view(),login_url="/"),name="create_new_category"),
    path('update-categoria/<int:pk>/',login_required(update_category_view.as_view(),login_url="/"),name="update_category"),
    path('delete-categoria/<int:pk>/',login_required(delete_category_view.as_view(),login_url="/"),name="delete_category"),
    path('detail-categoria/<int:pk>/',login_required(views.detail_category_view,login_url="/"),name="detail_category"),
    
]