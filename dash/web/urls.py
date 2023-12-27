from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic.base import TemplateView
from web.views import auth, home

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth.oauth_logout, name='logout'),

    #######  KEYCLOAK FRONT-CHANNEL LOGOUT URL  ########
    # path("_oauth/logout/", auth.oauth_logout),
    ####################################################

    path("", home.index, name="home"),
    path("dashboard/", home.dashboard, name="dashboard"),
    path("protected/", home.protected, name="protected"),
    path("public/", home.public, name="public"),

]
