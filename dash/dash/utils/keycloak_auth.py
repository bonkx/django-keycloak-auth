from django.conf import settings
from django.urls import reverse_lazy
from django.utils.http import urlencode


def provider_logout(request):
    host = "%s://%s" % (
        request.META['wsgi.url_scheme'],
        request.META['HTTP_HOST'],
    )
    # print(host)
    logout_url = settings.OIDC_OP_LOGOUT_ENDPOINT
    # return_to_url = request.build_absolute_uri(settings.LOGOUT_REDIRECT_URL)
    # return_to_url = request.build_absolute_uri(settings.LOGIN_REDIRECT_URL)
    return_to_url = request.build_absolute_uri(host)
    logout_request = f"{logout_url}?redirect_uri={return_to_url}"

    # print(logout_request)
    return logout_request
