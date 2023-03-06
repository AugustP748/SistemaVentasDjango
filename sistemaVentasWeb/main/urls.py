from django.contrib import admin
from django.urls import include, path
from . import views

app_name = "main"
urlpatterns = [
    path('',views.login_view,name="login_view"),
    path('',include('django.contrib.auth.urls'))
]