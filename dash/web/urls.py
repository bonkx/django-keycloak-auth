from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic.base import TemplateView
from web.views import home

urlpatterns = [
    path('login/', auth_views.LoginView.as_view()),
    path("", home.index, name="home"),
    path("protected/", home.protected, name="protected"),
    path("public/", home.public, name="public"),
]
