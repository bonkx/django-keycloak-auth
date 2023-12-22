from django.conf import settings
from django.urls import reverse_lazy
from django.utils.http import urlencode


def provider_logout(request):

    # I implemented logout using Keycloak 4.8.3 version. Mandatory parameter is id token (id_token_hint).
    # Optional parameter is redirect url (post_logout_redirect_uri). Example:

    # http: //my-auth-server/auth/realms/master/protocol/openid-connect/logout?
    # id_token_hint=eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJEY0gyNnl0OFV0OEJQTGxoR
    # &post_logout_redirect_uri=http:%2F%2Fapplication-root.com%2F

    id_token = request.session['oidc_id_token']
    print("id_token :", id_token)

    logout_url = settings.OIDC_OP_LOGOUT_ENDPOINT
    # return_to_url = request.build_absolute_uri(settings.LOGOUT_REDIRECT_URL)
    return_to_url = request.build_absolute_uri(settings.LOGIN_REDIRECT_URL)
    # return_to_url = request.build_absolute_uri(LOGIN_URL)
    # logout_request = \
    #     f'{settings.OIDC_OP_LOGOUT_ENDPOINT}?client_id={settings.OIDC_RP_CLIENT_ID}' \
    #     f'&redirect_uri={return_to_url}'
    logout_request = logout_url + '?' + \
        urlencode({'id_token_hint': id_token,
                  'post_logout_redirect_uri': return_to_url})
    print(logout_request)
    return logout_request
