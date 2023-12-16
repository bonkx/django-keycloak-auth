from django.conf import settings
from django.utils.http import urlencode


def provider_logout(request):
    id_token = str(request.COOKIES['csrftoken'])
    logout_url = settings.OIDC_OP_LOGOUT_ENDPOINT
    # return_to_url = request.build_absolute_uri(settings.LOGOUT_REDIRECT_URL)
    return_to_url = request.build_absolute_uri(settings.LOGIN_REDIRECT_URL)
    logout_request = \
        f'{settings.OIDC_OP_LOGOUT_ENDPOINT}?id_token_hint={id_token}' \
        f'&post_logout_redirect_uri={return_to_url}'
    # logout_request = logout_url + '?' + \
    #     urlencode({'redirect_uri': return_to_url,
    #               'client_id': settings.OIDC_RP_CLIENT_ID})
    print(logout_request)
    return logout_request
