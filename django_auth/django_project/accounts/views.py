from django.shortcuts import render

# Create your views here.
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("accounts/", auth_views.accountsView.as_view()),
]

urlpatterns = [
    path("accounts/", auth_views.accountsView.as_view()),
]