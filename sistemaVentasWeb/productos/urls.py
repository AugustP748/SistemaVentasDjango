from django.contrib import admin
from django.urls import path
#from .views import products_view,create_product_view, update_products_view, delete_products_view
from .views import products_view,create_product_view
from django.contrib.auth.decorators import login_required
from . import views


app_name = "productos"
urlpatterns = [
    path('productos/',login_required(products_view.as_view(),login_url="/"),name="products_view"),
    path('nuevo-producto/',login_required(create_product_view.as_view(),login_url="/"),name="create_new_product"),
    
]