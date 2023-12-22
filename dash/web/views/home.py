import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from login_required import login_not_required
from mozilla_django_oidc.auth import OIDCAuthenticationBackend

# Create your views here.


# def get_user_keycloak_info(request):
#     if 'oidc_access_token' not in request.session:
#         return None

#     oidc_access_token = request.session['oidc_access_token']
#     # print("oidc_access_token : ", oidc_access_token)
#     oidc_id_token = request.session['oidc_id_token']
#     # print("oidc_id_token : ", oidc_id_token)
#     user_response = requests.get(
#         settings.OIDC_OP_USER_ENDPOINT,
#         headers={"Authorization": "Bearer {0}".format(oidc_access_token)},
#     )
#     user_response.raise_for_status()
#     return user_response.json()


@login_not_required
def public(request):
    return render(request, "web/public.html", {})


# @login_required
def index(request):
    # user = request.user
    # print(settings.KC_BASE_URI)
    # user_info = get_user_keycloak_info(request)
    # print(user_info)
    # if not user_info:
    #     redirect('protected')
    # response = requests.get(discovery_url)
    # # response = requests.get(discovery_url, verify=False)
    # if response.status_code != 200:
    #     raise ValueError("Failed to retrieve provider configuration.")
    return render(request, "web/home.html", {})


# @login_required
def protected(request):
    return render(request, "web/protect.html", {})
