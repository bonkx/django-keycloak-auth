
from api.paginations import CustomPagination
from api.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import authentication, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from dash.utils import keycloak

# Create your views here.


@api_view(['GET'])
def me(request):
    # 401 "detail": "Token verification failed"

    # GET KEYCLOAK USER INFO
    auth = authentication.get_authorization_header(request).split()
    # print(auth)
    access_token = auth[1]

    keycloak_response = keycloak.get_keycloak_info(access_token.decode())
    # print(keycloak_response)
    if keycloak_response.status_code != 200:
        return Response({"detail": "Token verification failed!"}, status=401)

    keycloak_info = keycloak_response.json()
    # print(keycloak_info)
    ################################

    # add keycloak_info to UserSerializer
    srz = UserSerializer(request.user, many=False,
                         context={"keycloak_info": keycloak_info})
    return Response(srz.data)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def list_users(request):
    paginator = CustomPagination()
    paginator.page_size = 10

    data = User.objects.all().order_by('id')

    result_page = paginator.paginate_queryset(data, request)

    srz = UserSerializer(result_page, many=True)
    return paginator.get_paginated_response(srz.data)


class UserViewSet(viewsets.ModelViewSet):
    model = User
    queryset = model.objects.all().order_by('id')
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', ]
