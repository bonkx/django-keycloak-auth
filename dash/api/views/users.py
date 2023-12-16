
from api.paginations import CustomPagination
from api.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def me(request):
    # 401 "detail": "Token verification failed"
    srz = UserSerializer(request.user, many=False)
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
