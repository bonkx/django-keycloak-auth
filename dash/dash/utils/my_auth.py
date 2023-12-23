from django.conf import settings
from django.contrib import auth
from django.http import HttpResponseRedirect, request
from django.urls import reverse_lazy
from django.utils.http import urlencode
from mozilla_django_oidc.utils import is_authenticated


def provider_logout(request):

    # I implemented logout using Keycloak 4.8.3 version. Mandatory parameter is id token (id_token_hint).
    # Optional parameter is redirect url (post_logout_redirect_uri). Example:

    # http: //my-auth-server/auth/realms/master/protocol/openid-connect/logout?
    # id_token_hint=eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJEY0gyNnl0OFV0OEJQTGxoR
    # &post_logout_redirect_uri=http:%2F%2Fapplication-root.com%2F

    id_token = request.session['oidc_id_token']
    print("id_token :", id_token)

    logout_url = settings.OIDC_OP_LOGOUT_ENDPOINT
    return_to_url = request.build_absolute_uri(settings.LOGIN_REDIRECT_URL)
    # return_to_url = settings.LOGIN_REDIRECT_URL
    # logout_request = logout_url + '?' + \
    #     urlencode({'id_token_hint': id_token,
    #               'post_logout_redirect_uri': return_to_url})
    logout_request = logout_url + '?' + \
        urlencode({'client_id': settings.OIDC_RP_CLIENT_ID,
                  'post_logout_redirect_uri': return_to_url})
    print(logout_request)
    return logout_request


def get_logout_url(request):
    '''
    Return the url of the logout for keycloak
    '''
    keycloak_redirect_url = settings.OIDC_OP_LOGOUT_ENDPOINT or None
    return f"{keycloak_redirect_url}?redirect_uri=" + request.build_absolute_uri("/")


def keycloak_logout(request):
    '''
    Perform the logout of the app and redirect to keycloak
    '''
    django_logout_url = settings.LOGOUT_REDIRECT_URL or '/'

    if is_authenticated(request.user):
        logout_url = get_logout_url(request)

        # Log out the Django user if they were logged in.
        auth.logout(request)

        return HttpResponseRedirect(logout_url)
