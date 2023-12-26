import requests
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from login_required import login_not_required
from mozilla_django_oidc.auth import OIDCAuthenticationBackend


def oauth_logout(request):
    # print('Loggin out {}'.format(request.user))
    auth.logout(request)
    # print(request.user)
    # return HttpResponseRedirect('/')
    return redirect(reverse('home'))
