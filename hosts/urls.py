from django.urls import path
from django.conf.urls import include
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = "hosts"
urlpatterns = [
    #url(r"^login/", views.LoginView.as_view(), name='login'),
    path("", views.LoginView.as_view(), name="login"),
    url(r"^hostTable/", views.hostTable, name="Host"),
]
