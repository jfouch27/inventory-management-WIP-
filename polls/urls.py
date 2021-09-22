from django.urls import path
from django.conf.urls import include
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = "polls"
urlpatterns = [
    url(r"^login/", views.LoginView.as_view(), name='login'),
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    url(r"^hostTable/", views.hostTable, name="Host"),
    url(
        r"^dataTable/",
        views.HostView.as_view(),
        name="HostTable",
    ),
]
