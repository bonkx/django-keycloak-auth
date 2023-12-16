

from api.serializers import UserSerializer
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['POST'])
@permission_classes((AllowAny, ))
def register(request):
    print(request.data)
    # Step 1. Login Admin
    # Step 2. Create user by Admin
    return Response({"detail": "Sukses!!!"})
