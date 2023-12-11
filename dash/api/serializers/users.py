from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='get_full_name')

    class Meta:
        model = User
        # fields = ('username', 'email', 'id', 'name', 'password')
        # fields = '__all__'
        read_only_fields = ('id',)
        exclude = ['groups', 'user_permissions']
        extra_kwargs = {
            'password': {'write_only': True}
        }
