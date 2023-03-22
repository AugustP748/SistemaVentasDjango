from django.contrib import admin
from django.urls import path
#from .views import products_view,create_product_view, update_products_view, delete_products_view
from .views import *
from django.contrib.auth.decorators import login_required
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "productos"
urlpatterns = [
    path('productos/',login_required(products_view.as_view(),login_url="/"),name="products_view"),
    path('nuevo-producto/',login_required(create_product_view.as_view(),login_url="/"),name="create_new_product"),
    path('update-producto/<int:pk>/',login_required(update_product_view.as_view(),login_url="/"),name="update_product"),
    path('delete-producto/<int:pk>/',login_required(delete_product_view.as_view(),login_url="/"),name="delete_product"),
    path('detail-producto/<int:pk>/',login_required(detail_product_view.as_view(),login_url="/"),name="detail_product"),
    path('categorias/',login_required(Categories_view.as_view(),login_url="/"),name="categories_view"),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)