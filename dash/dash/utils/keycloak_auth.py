from django.conf import settings
from django.urls import reverse_lazy
from django.utils.http import urlencode

# app/auth.py


def provider_logout(request):
    """ Create the user's OIDC logout URL."""
    # User must confirm logout request with the default logout URL
    # and is not redirected.
    logout_url = settings.OIDC_OP_LOGOUT_ENDPOINT
    logout_redirect_uri = settings.LOGIN_REDIRECT_URL

    # If we have the oidc_id_token, we can automatically redirect
    # the user back to the application.
    oidc_id_token = request.session.get('oidc_id_token', None)
    # print(oidc_id_token)
    if oidc_id_token:
        logout_url = (
            settings.OIDC_OP_LOGOUT_ENDPOINT
            + "?"
            + urlencode({"id_token_hint": oidc_id_token,
                        "post_logout_redirect_uri": request.build_absolute_uri(logout_redirect_uri)})
        )
    else:
        logout_url = (
            settings.OIDC_OP_LOGOUT_ENDPOINT
            + "?"
            + urlencode({"client_id": settings.OIDC_RP_CLIENT_ID,
                        "post_logout_redirect_uri": request.build_absolute_uri(logout_redirect_uri)})
        )

    return logout_url
