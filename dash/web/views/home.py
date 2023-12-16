from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# from login_required import login_not_required

# Create your views here.


# @login_not_required
def public(request):
    return render(request, "web/public.html", {})


@login_required
def index(request):
    # user = request.user
    # oidc_access_token = request.session['oidc_access_token']
    # print("oidc_access_token : ", oidc_access_token)
    # oidc_id_token = request.session['oidc_id_token']
    # print("oidc_id_token : ", oidc_id_token)
    # print(settings.KC_BASE_URI)
    return render(request, "web/home.html", {})


@login_required
def protected(request):
    return render(request, "web/protect.html", {})
